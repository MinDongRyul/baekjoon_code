import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '.':
        break
    stack = []
    yes_true = True
    for unit in string:
        if unit in '([':
            stack.append(unit)
        elif (unit == ')' and (not stack or stack[-1] == '[')) or (unit == ']' and (not stack or stack[-1] == '(')):
            yes_true = False
            break
        elif (unit == ')' and stack[-1] == '(') or (unit == ']' and stack[-1] == '['):
            stack.pop()

    if yes_true and not stack:
        print('yes')
    else:
        print('no')