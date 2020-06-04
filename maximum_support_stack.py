# https://www.dropbox.com/s/blcqv12qprz0hk7/statements.pdf?dl=0
# задача 2.4


stack = [0]

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        command = input().split()
        if command[0] == 'push':
            maximum = max(stack[-1], int(command[1]))
            stack.append(maximum)
        elif command[0] == 'pop':
            stack.pop()
        else:
            print(stack[-1])
