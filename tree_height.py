# https://www.dropbox.com/s/blcqv12qprz0hk7/statements.pdf?dl=0
# задача 2.2
tree = []
height_max = 0

if __name__ == '__main__':
    _ = input()
    tree = list(map(int, input().split()))
    for i in tree:
        parent = i
        height = 1
        while parent != -1:
            parent = tree[parent]
            height += 1
        if height > height_max:
            height_max = height
    print(height_max)
