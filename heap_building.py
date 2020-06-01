# https://www.dropbox.com/s/blcqv12qprz0hk7/statements.pdf?dl=0
# задача 3.1
# Переставить элементы заданного массива чисел так, чтобы он удовле-
# творял свойству мин-кучи


class MinHeap:
    heap = []
    swaps = []

    @staticmethod
    def _l_child_index(i):
        return 2 * i + 1

    def _l_child(self, i):
        return self.heap[self._l_child_index(i)]

    @staticmethod
    def _r_child_index(i):
        return 2 * i + 2

    def _r_child(self, i):
        return self.heap[self._r_child_index(i)]

    def sift_down(self, i):
        min_index = i
        l_child_index = self._l_child_index(i)
        if l_child_index < len(self.heap) and self._l_child(i) < self.heap[
            min_index]:
            min_index = l_child_index

        r_child_index = self._r_child_index(i)
        if r_child_index < len(self.heap) and self._r_child(i) < self.heap[
            min_index]:
            min_index = r_child_index

        if i != min_index:
            self.heap[i], self.heap[min_index] = \
                self.heap[min_index], self.heap[i]
            self.swaps.append((i, min_index))
            self.sift_down(min_index)

    def __init__(self, arr):
        self.heap = arr
        for i in range(int((len(arr)) / 2) - 1, -1, -1):
            self.sift_down(i)


def main():
    input()
    a = [int(i) for i in input().split()]
    min_heap = MinHeap(a)
    print(len(min_heap.swaps))
    for i in min_heap.swaps:
        print(*i)


if __name__ == '__main__':
    main()
