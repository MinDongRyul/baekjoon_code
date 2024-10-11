def func(N : int, K : int) -> int:
    rank = 1
    medal = [list(map(int, input().split())) for _ in range(N)]
    medal = sorted(medal, key=lambda x : [x[1], x[2], x[3]], reverse=True)
    
    for idx in range(len(medal)-1):
        if medal[idx][0] == K:
            break
        if medal[idx][1:] != medal[idx+1][1:]:
            rank += 1
    return rank

N, K = map(int, input().split())
print(func(N, K))