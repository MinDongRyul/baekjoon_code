N, new_score, P = map(int, input().split())
if N == 0:
    print(1)
else:
    current_scores = list(map(int, input().split()))
    current_scores = sorted(current_scores + [new_score], reverse=True)
    if current_scores.index(new_score) + current_scores.count(new_score) > P:
        print(-1)
    else:
        print(current_scores.index(new_score) + 1)