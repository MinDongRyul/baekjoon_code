from typing import List
def func(save:List[int], N:int, L:int) -> int:
    save = sorted(save)
    check = [1] * 1001
    total = 0
    for idx in range(N):
        if check[save[idx]]:
            for save_idx in range(save[idx], save[idx]+L):
                if save_idx < 1001:
                    check[+save_idx] = 0
            total += 1
    return total

N, L = map(int, input().split())
save = list(map(int, input().split()))
print(func(save, N, L))