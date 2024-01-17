from Uint128 import Uint128

def readKeysFromCSV(file: str) -> list[Uint128]:
    """Reads keys from a CSV file and returns them as a list of Uint128"""
    keys = []
    with open(file, 'r') as f:
        for line in f:
            keys.append(Uint128(line.strip()))
    return keys