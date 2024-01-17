import timeit
from readKeys import readKeysFromCSV
import random
from BinomialHeap import BinomialHeap
from matplotlib import pyplot as plt

list_sizes = [500000, 1000000, 2000000, 2500000, 3000000, 3500000]
hash_dict = {}


def generate_keys():
    for size in list_sizes:
        with open("./cles_big/random" + str(size) + ".txt", "w") as f:
            for i in range(size):
                key = hex(random.getrandbits(128))
                while key in hash_dict:
                    key = hex(random.getrandbits(128))
                hash_dict[key] = True
                f.write(str(key) + "\n")
        f.close()


def union_test():
    times = []
    for size in list_sizes:
        keys = readKeysFromCSV("./cles_big/random" + str(size) + ".txt")
        heap1 = BinomialHeap()
        heap1.createBinomialHeap(keys[:size//2])
        heap2 = BinomialHeap()
        heap2.createBinomialHeap(keys[size//2:])
        times.append(timeit.timeit(lambda: heap1.mergeHeap(heap2), number=1))
    return times


if __name__ == "__main__":
    times = union_test()
    plt.plot(list_sizes, times)
    plt.xlabel("Size of Data (Number of Keys)")
    plt.ylabel("Average Execution Time (seconds)")
    plt.title("Union")
    plt.show()
