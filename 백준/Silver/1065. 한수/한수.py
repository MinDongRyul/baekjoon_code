N = int(input())
if N < 100:
    print(N)
else:
    T = 99
    for x in range(100, N+1):
        x = str(x)
        if int(x[0]) - int(x[1]) == int(x[1]) - int(x[2]):
            T += 1
    print(T)