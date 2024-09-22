import sys
w = [0 for _ in range(105)]
v = [0 for _ in range(105)]
dp = [[0 for _ in range(100005)] for _ in range(105)]

n, k = map(int, sys.stdin.readline().split())
for i in range(1, n+1):
    w[i], v[i] = map(int, sys.stdin.readline().split())
for i in range(1, n+1):
    for j in range(1, k+1):
        if j-w[i] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])