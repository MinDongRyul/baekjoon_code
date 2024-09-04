n = int(input())
wait = list(map(int, input().split()))
stack = [1001]
last = []
idx = 1

while wait:
    first_wait = wait[0]
    last_stack = stack[-1]
    if first_wait == idx:
        last.append(first_wait)
        wait.remove(first_wait)
        idx += 1
    elif last_stack == idx:
        last.append(last_stack)
        stack.remove(last_stack)
        idx += 1
    else:
        stack.append(first_wait)
        wait.remove(first_wait)

stack = stack[::-1][:-1]
if stack == sorted(stack):
    print('Nice')
else:
    print('Sad')