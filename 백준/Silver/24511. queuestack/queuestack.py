N = int(input())
queue_stack = list(map(int, input().split()))
raw = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

real_use = [raw[idx] for idx in range(N) if queue_stack[idx] == 0][::-1]
result = []
for unit in C:
    real_use.append(unit)

for idx in range(M):
    print(real_use[idx], end = ' ')