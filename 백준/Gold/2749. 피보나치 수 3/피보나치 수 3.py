def fibo(n, cycle, d : int = 10 ** 6):
    return (cycle[n-1] + cycle[n-2]) % d

N = int(input())
p = 1500000
cycle = [0] * p
cycle[0] = 0
cycle[1] = 1

for idx in range(2, (N%p)+1):
    cycle[idx] = fibo(idx, cycle)

if N >= p:
    N %= p

print(cycle[N])