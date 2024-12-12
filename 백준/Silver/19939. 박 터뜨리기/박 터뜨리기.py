import sys
input = sys.stdin.readline

def func(N : int, K : int) -> int:
    
    pre_sum = K * (K + 1) // 2

    if pre_sum > N:
        print(-1)
    elif (N - pre_sum) % K == 0:
        print(K-1)
    else:
        print(K)
    
N, K = map(int, input().rstrip().split())
func(N, K)