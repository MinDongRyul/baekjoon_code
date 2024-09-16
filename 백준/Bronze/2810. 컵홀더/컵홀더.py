N = int(input())
info = input()
if 'LL' in info:
    print(info.count('LL') + info.count('S') + 1)
else:
    print(N)