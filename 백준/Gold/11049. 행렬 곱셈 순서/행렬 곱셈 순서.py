import sys
input = sys.stdin.readline

r, c = [], []
dp = [[0] * 500 for _ in range(500)]

def mat_mul(x, y):
    
    if dp[x][y] > 0 :
        return dp[x][y]
    
    if y - x <= 0:
        return 0
    
    mm = 2 ** 31 - 1
    for idx in range(x, y, 1):
        mm = min(mm, mat_mul(x, idx) + mat_mul(idx + 1, y) + r[x] * c[idx] * c[y])
    dp[x][y] = mm
    return dp[x][y]
    
N = int(input())
for _ in range(N):
    r_, c_ = map(int, input().split())
    r.append(r_)
    c.append(c_)

print(mat_mul(0, N-1))