import sys

n = int(input())
input=sys.stdin.readline

stack = []

for _ in range(n):
    num = input().rstrip().split()
    if num[0] == '1':
        stack.append(num[-1])
    elif num[0] == '2':
        if stack:
            last = stack.pop()
            print(int(last))
        else:
            print(-1)
    elif num[0] == '3':
        print(len(stack))
    elif num[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif num[0] == '5':
        if stack:
            print(int(stack[-1]))
        else:
            print(-1)