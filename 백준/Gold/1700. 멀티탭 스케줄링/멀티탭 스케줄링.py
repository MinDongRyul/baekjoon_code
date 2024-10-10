N, K = map(int, input().split())
wait = list(map(int, input().split()))
multi = []
final = 0

for k_idx in range(K):
    use = wait[k_idx]
    # 초기 세팅
    if len(multi) < N and use not in multi:
        multi.append(use)
    elif use in multi:
        # 원하는 기기가 멀티탭에 있으면 패스
        continue
    else:
        # 없는 경우 무엇을 제거해야 할지 결정
        farthest, change_idx = -1, -1
        for multi_idx, multi_value in enumerate(multi):
            # 앞으로 사용되지 않을 기기가 있다면 그것을 제거
            if multi_value not in wait[k_idx+1:]:
                change_idx = multi_idx
                break
            # 가장 나중에 등장하는 기기를 찾음
            else:
                next_use = wait[k_idx+1:].index(multi_value)
                if next_use > farthest:
                    farthest = next_use
                    change_idx = multi_idx

        # 기기 교체
        multi[change_idx] = use
        final += 1

print(final)