def mat_mul(A, B, N, D : int = 1000):
    rst = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for z in range(N):
                rst[x][y] += (A[x][z] * B[z][y])
            rst[x][y] %= D
    return rst
    
N, B = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

rst = [[0] * N for _ in range(N)]
for i in range(N):
    rst[i][i] = 1
    
while B != 0:
    if B % 2 == 1:
        rst = mat_mul(rst, arr, N)
    arr = mat_mul(arr, arr, N)
    B >>= 1

for item in rst:
    for value in item:
        print(value, end=' ')
    print()