def func(arr : int) -> int:
    total = 0
    for arr_ in arr:
        temp = 0
        for idx in range(len(arr_) - 1):
            current, future = arr_[idx], arr_[idx+1]
            if current == future and current != 'X':
                temp += 1
            elif temp > 0 and current != future:
                temp = 0
                total += 1
        if temp > 0:
            total += 1
    return total

N = int(input())
arr = []
temp = [[0] * N for _ in range(N)]
for _ in range(N):
    arr.append(input())
    
for x in range(len(arr)):
    for y in range(len(arr)):
        temp[x][y] = arr[y][x]
    
print(func(arr), func(temp))