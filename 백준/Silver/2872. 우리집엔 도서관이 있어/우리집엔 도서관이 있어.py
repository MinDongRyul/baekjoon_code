import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

max_val = max(arr) 
max_idx = arr.index(max_val)

# 큰 값보다 아래 작은 수로 카운트하기위함?
sort_cnt = 1
for i in range(max_idx - 1, -1, -1):
    if arr[i] == max_val - sort_cnt:
        sort_cnt += 1

# 정렬된 갯수를 뺸 나머지를 '알아서' 뽑아서 정렬함
print(N - sort_cnt)