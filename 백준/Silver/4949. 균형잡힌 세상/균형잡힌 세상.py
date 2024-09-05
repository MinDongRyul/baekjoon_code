while True:
    string = input()
    if string == '.':
        break
    stack = []
    yes_true = True
    for unit in string:
        if unit.isalpha() or unit.isspace():
            pass
        elif unit == '(' or unit == '[':
            stack.append(unit)
        elif unit == ')':
            if not stack or stack[-1] == '[':
                yes_true = False
                break
            else:
                stack.pop()
        elif unit == ']':
            if not stack or stack[-1] == '(':
                yes_true = False
                break
            else:
                stack.pop()
    if yes_true and not stack:
        print('yes')
    else:
        print('no')