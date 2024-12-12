N, B = map(int, input().split())
save = []
while N > 0:
    save.append(chr(55 + (N % B)) if N % B >= 10 else str(N % B))
    N //= B
rst = ''.join(save[::-1])
print(rst)