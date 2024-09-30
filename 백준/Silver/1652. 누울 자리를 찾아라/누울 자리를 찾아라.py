def func(arr : int) -> int:
    total = 0
    for arr_ in arr:
        temp = 0
        for idx in range(len(arr_) - 1):
            cur, nex = arr_[idx], arr_[idx+1]
            if cur == nex and cur != 'X':
                temp += 1
            elif temp > 0 and cur != nex:
                temp = 0
                total += 1
        if temp > 0:
            total += 1
    return total

N = int(input())
ver = []
hori = [[0] * N for _ in range(N)]
for _ in range(N):
    ver.append(input())
    
for x in range(N):
    for y in range(N):
        hori[x][y] = ver[y][x]
    
print(func(ver), func(hori))