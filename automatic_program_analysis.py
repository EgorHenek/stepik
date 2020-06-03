# Решение https://www.dropbox.com/s/blcqv12qprz0hk7/statements.pdf?dl=0
# Задача 4.2


class DisjointSet:
    parents = []
    ranks = []

    def __init__(self, n):
        for i in range(n):
            self.parents.append(i)
            self.ranks.append(0)

    def find(self, i):
        while i != self.parents[i]:
            i = self.parents[i]
        return i

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id != j_id:
            if self.ranks[i_id] > self.ranks[j_id]:
                self.parents[j_id] = i_id
            else:
                self.parents[i_id] = j_id
            if self.ranks[i_id] == self.ranks[j_id]:
                self.ranks[j_id] += 1


def main():
    n, e, d = [int(i) for i in input().split(' ')]
    dset = DisjointSet(n)
    for _ in range(e):
        i, j = [int(i) - 1 for i in input().split(' ')]
        dset.union(i, j)
    for _ in range(d):
        i, j = [int(i) - 1 for i in input().split(' ')]
        if dset.find(i) == dset.find(j):
            print(0)
            break
    else:
        print(1)


if __name__ == '__main__':
    main()
