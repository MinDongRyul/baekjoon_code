n = int(input())
wait = list(map(int, input().split()))
stack = [1001]
last = []

while wait:
    first_wait = wait[0]
    last_stack = stack[-1]
    if first_wait == min(stack+wait):
        last.append(first_wait)
        wait.remove(first_wait)
    elif last_stack == min(stack+wait):
        last.append(last_stack)
        stack.remove(last_stack)
    else:
        stack.append(first_wait)
        wait.remove(first_wait)

stack = stack[::-1][:-1]
if stack == sorted(stack):
    print('Nice')
else:
    print('Sad')