# Решение https://www.dropbox.com/s/blcqv12qprz0hk7/statements.pdf?dl=0
# Задача 4.1
# Решение через непересекающиеся множества со сжатием путей


class DisjointSet:
    parents = []
    ranks = []
    maximum = 0

    def __init__(self, lst):
        for i in range(len(lst)):
            self.parents.append(i)
        self.ranks = lst
        self.maximum = max(lst)

    def find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id != j_id:
            self.parents[j_id] = i_id
            new_rank = self.ranks[i_id] + self.ranks[j_id]
            self.ranks[i_id] = new_rank
            self.ranks[j_id] = new_rank

            if new_rank > self.maximum:
                self.maximum = new_rank
        print(self.maximum)


def main():
    n, m = [int(i) for i in input().split(' ')]
    dset = DisjointSet([int(i) for i in input().split(' ')])
    for _ in range(m):
        dset.union(*[int(i) - 1 for i in input().split(' ')])


if __name__ == '__main__':
    main()
