def sortiSR(array) -> None:
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

if __name__ == '__main__':
    from random import randint
    from math import sqrt
    import time
    for i in range(100, 1000, 100):
        print("---", i, "---")
        for l in range(1, 31):
            a = [0 * t for t in range(i)]
            for k in range(i):
                a.append(randint(100, 1000))
            start = time.perf_counter()
            p = sortiSR(a)
            end = time.perf_counter()
            d = end - start
            print(f"{d:.8f}")
        print("-------")

