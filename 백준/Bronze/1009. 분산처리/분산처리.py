mod = []
for idx in range(1, 11):
    mods = [idx ** 1 % 10, idx ** 2 % 10, idx ** 3 % 10, idx ** 4 % 10]
    mod.append(list(mods))
    
for _ in range(int(input())):
    A, B = map(int, input().split())
    A %= 10
    mod_ = B % len(set(mod[A-1]))
    print(mod[A-1][mod_-1] if mod[A-1][mod_-1] else 10)