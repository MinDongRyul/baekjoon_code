from typing import List
import sys
input = sys.stdin.readline

def comparison(value_1 : List[int], value_2 : List[int], rank : int) -> int:
    if len(value_1) == 0:
        return rank
    if value_1[0] > value_2[0]:
        rank += 1
        return rank
    elif value_1[0] < value_2[0]:
        return rank
    else:
        return comparison(value_1[1:], value_2[1:], rank)

def func(N : int, K : int) -> int:
    rank = 1
    medal = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]
    for value in medal:
        if value[0] == K:
            save = value
            break
    for value in medal:
        rank = comparison(value[1:], save[1:], rank)
    return rank

N, K = map(int, input().rstrip('\n').split())
print(func(N, K))
