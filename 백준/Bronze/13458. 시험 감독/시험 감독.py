from typing import List
import math

def func(A : List[int], B : int, C : int) -> int:
    tot = 0
    for people in A:
        if people - B <= 0:
            tot += 1
        else:
            tot += math.ceil((people - B) / C) + 1
    return tot

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
print(func(A, B, C))