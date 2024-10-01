from typing import List
def func(arr : List) -> int:
    total = 0
    for arr_ in arr:
        total += len([bed for bed in ''.join(arr_).split('X') if len(bed) > 1])
    return total

N = int(input())
arr = []
for _ in range(N):
    arr.append(input())
    
print(func(arr), func(zip(*arr)))
