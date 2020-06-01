# Решение https://www.dropbox.com/s/blcqv12qprz0hk7/statements.pdf?dl=0
# Задача 3.2
from queue import PriorityQueue


def main():
    cpu_count, n = (int(i) for i in input().split(' '))
    arr = [int(i) for i in input().split(' ')]

    queue = PriorityQueue(cpu_count)
    for cpu in range(0, cpu_count):
        queue.put((0, cpu))

    for process in arr:
        cpu = queue.get()
        print(cpu[1], cpu[0])
        queue.put((process + cpu[0], cpu[1]))


if __name__ == '__main__':
    main()
