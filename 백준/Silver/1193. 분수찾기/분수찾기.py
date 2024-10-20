def func(N : int) -> str:
    
    range_num, range_sum = 0, 0

    while N > range_sum:
        range_num += 1
        range_sum = range_num * (range_num + 1) // 2
       
    # 짝수
    if range_num % 2 == 0:
        return '{}/{}'.format(N - (range_sum - range_num), (range_num + 1) - (N - (range_sum - range_num)))
    # 홀수
    else:
        return '{}/{}'.format((range_num + 1) - (N - (range_sum - range_num)), N - (range_sum - range_num))

N = int(input())
print(func(N))