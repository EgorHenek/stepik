# Решение https://www.dropbox.com/s/blcqv12qprz0hk7/statements.pdf?dl=0
# Задача 2.1


brackets = ['[', '{', '(', ']', '}', ')']
stack = []

if __name__ == '__main__':
    string = input()
    for n, symbol in enumerate(string, start=1):
        if symbol not in brackets:
            continue

        if symbol in brackets[:3]:
            stack.append((symbol, n))
        elif not stack:
            print(n)
            break
        else:
            index = brackets.index(symbol)
            if stack.pop()[0] != brackets[index - 3]:
                print(n)
                break
    else:
        if stack:
            print(stack.pop()[1])
        else:
            print('Success')
