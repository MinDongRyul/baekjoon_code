import sys
input = sys.stdin.readline

def func(N : int, K : int) -> int:
    rank = 1
    medal = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]
    for value in medal:
        if value[0] == K:
            save = value
            break
    
    for value in medal:
        if value[1] > save[1]:
            rank += 1
            continue
        elif value[1] < save[1]:
            continue
        else:
            if value[2] > save[2]:
                rank += 1
                continue
            elif value[2] < save[2]:
                continue
            else:
                if value[3] > save[3]:
                    rank += 1
                    continue
                elif value[3] < save[3]:
                    continue
        
    return rank

N, K = map(int, input().rstrip('\n').split())
print(func(N, K))