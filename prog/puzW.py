
def sortiW(array) -> None:
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


if __name__ == '__main__':
    import time
    d = 0
    for h in range(100, 1100, 100):
        a = [i for i in range(h, 0, -1)]
        start = time.perf_counter()
        p = sortiW(a)
        end = time.perf_counter()
        d = end-start
        print(f"{(d):.6f}")




