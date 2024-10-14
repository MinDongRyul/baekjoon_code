def fn(N : str) -> int:
    if len(N) < 2:
        N = '0' + N
    copy_N = N
    cycle = 0
    while True:
        temp_N = int(N[0]) + int(N[1]) 
        N = N[1] + str(temp_N)[-1]
        cycle +=1
        if N == copy_N:
            break
    return cycle

print(fn(input()))