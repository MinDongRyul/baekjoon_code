N, M = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
current_sum = 0
left = 0

for right in range(N):
    current_sum += nums[right]

    while current_sum > M:
        current_sum -= nums[left]
        left += 1
    
    if current_sum == M:
        cnt += 1

print(cnt)
