def facto(n, k, result):
    if n >= k:
        return result
    return facto(n+1, k, result * (n+1))

n = int(input())
print(facto(1, n, 1))