import numpy as np


class Uint128:
    def __init__(self, hexString: str) -> None:
        self.value = np.array(
            divmod(int(hexString, 16), 2**64), dtype=np.uint64)

    def __str__(self) -> str:
        val = self.value[0] * 2**64 + self.value[1]
        return val.__str__()

    def inf(self, other: 'Uint128') -> bool:
        if (self.value[0] < other.value[0]):
            return True
        elif (self.value[0] == other.value[0]):
            if (self.value[1] < other.value[1]):
                return True
            else:
                return False
        return False

    def egal(self, other: 'Uint128') -> bool:
        if (self.value[0] == other.value[0] and self.value[1] == other.value[1]):
            return True
        return False
