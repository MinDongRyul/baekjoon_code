import sys
input = sys.stdin.readline

def func(scores, N):
    scores = sorted(scores, key=lambda x : x[0])
    fin = 0
    for score in scores:
        if score[1] <= N:
            N = score[1]
            fin += 1
    return fin
    
T = int(input())
for _ in range(T):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]    
    print(func(scores, N))