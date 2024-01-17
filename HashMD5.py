# Write MD5 hash function from scratch
# Pseudocode: //Note : Toutes les variables sont sur 32 bits

# Définir r comme suit:
# var entier[64] r, k
# r[0..15] := {7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22}
# r[16..31] := {5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20}
# r[32..47] := {4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23}
# r[48..63] := {6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21}

# MD5 utilise des sinus d'entiers pour ses constantes:
# pour i de 0 à 63 faire
#    k[i] := floor(abs(sin(i + 1)) × 2 ^ 32)
# fin pour

# Préparation des variables:
# var entier h0 := 0x67452301
# var entier h1 := 0xEFCDAB89
# var entier h2 := 0x98BADCFE
# var entier h3 := 0x10325476

# Préparation du message(padding):
# ajouter le bit "1" au message
# ajouter le bit "0" jusqu'à ce que la taille du message en bits soit égale à 448 (mod 512)
# ajouter la taille du message initial(avant le padding) codée en 64-bit little-endian au message

# Découpage en blocs de 512 bits:
# pour chaque bloc de 512 bits du message
#    subdiviser en 16 mots de 32 bits en little-endian w[i], 0 ≤ i ≤ 15

#     initialiser les valeurs de hachage:
#     var entier a := h0
#     var entier b := h1
#     var entier c := h2
#     var entier d := h3

#     Boucle principale:
#     pour i de 0 à 63 faire
#        si 0 ≤ i ≤ 15 alors
#              f := (b et c) ou((non b) et d)
#               g := i
#         sinon si 16 ≤ i ≤ 31 alors
#              f := (d et b) ou ((non d) et c)
#               g := (5×i + 1) mod 16
#         sinon si 32 ≤ i ≤ 47 alors
#              f := b xor c xor d
#               g := (3×i + 5) mod 16
#         sinon si 48 ≤ i ≤ 63 alors
#            f := c xor (b ou (non d))
#             g := (7×i) mod 16
#         fin si
#         var entier temp := d
#         d := c
#         c := b
#         b := leftrotate((a + f + k[i] + w[g]), r[i]) + b
#         a := temp
#     fin pour

#     ajouter le résultat au bloc précédent:
#     h0 := h0 + a
#     h1 := h1 + b
#     h2 := h2 + c
#     h3 := h3 + d
# fin pour
# var entier empreinte := h0 concaténer h1 concaténer h2 concaténer h3 // (en little-endian)
from math import floor, sin


class HashMD5:
    def __init__(self):
        self.rotate = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                       5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
                       4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                       6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
        # Use binary integer part of the sines of integers (Radians) as constants:
        # & 0xFFFFFFFF is to get the last 32 bits
        self.constants = [int(abs(sin(i+1)) * 4294967296)
                          & 0xFFFFFFFF for i in range(64)]
        self.buffer = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

    # Pre-processing:
    def _pad(self, message: str) -> str:
        # Length of message (before pre-processing) in bits
        message_bit_length = (8*len(message)) & 0xffffffffffffffff
        # Pre-processing: adding a single 1 bit
        message.append(0x80)

        # Pre-processing: padding with zeros
        while len(message) % 64 != 56:
            message.append(0)

        # Pre-processing: appending length
        message += message_bit_length.to_bytes(8, byteorder='little')

        return message
    # Leftrotate as defined in RFC is circular shift, but python's shift is not circular

    def _left_rotate(self, x: int, amount: int) -> int:
        # Rotate left
        x &= 0xFFFFFFFF
        return (x << amount | x >> (32-amount)) & 0xFFFFFFFF

    def _process_message(self, message: str) -> str:
        temp_buffer = self.buffer.copy()
        for block512 in range(0, len(message), 64):
            a, b, c, d = temp_buffer
            block = message[block512:block512+64]
            for i in range(64):
                if i >= 0 and i <= 15:
                    f = (b & c) | ((~b) & d)
                    g = i
                elif i >= 16 and i <= 31:
                    f = (d & b) | ((~d) & c)
                    g = (5*i + 1) % 16
                elif i >= 32 and i <= 47:
                    f = b ^ c ^ d
                    g = (3*i + 5) % 16
                elif i >= 48 and i <= 63:
                    f = c ^ (b | (~d))
                    g = (7*i) % 16
                temp = d
                d = c
                c = b
                rotate_by = (a + f + self.constants[i] +
                             int.from_bytes(block[4*g:4*g+4], byteorder='little'))
                b = (self._left_rotate((rotate_by),
                     self.rotate[i]) + b) & 0xFFFFFFFF
                a = temp

            for index, value in enumerate([a, b, c, d]):
                temp_buffer[index] += value
                temp_buffer[index] &= 0xFFFFFFFF
        # Convert temp_buffer to message
        return sum(x << (32*i) for i, x in enumerate(temp_buffer))

    # Convert message to little endian and to hex
    def _digest(self, message: str) -> str:
        message_bit = message.to_bytes(16, byteorder='little')
        return '{:032x}'.format(int.from_bytes(message_bit, byteorder='big'))

    def hash(self, message: str) -> str:
        message = bytearray(message, 'utf-8')
        return self._digest(self._process_message(self._pad(message)))


if __name__ == "__main__":
    hashMD5 = HashMD5()
    print(hashMD5.hash('Et l’unique cordeau des trompettes marines'))
