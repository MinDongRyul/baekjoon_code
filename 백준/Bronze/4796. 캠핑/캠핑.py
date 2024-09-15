idx = 1
while True:
    L, P, V = map(int, input("").split())
    if L == 0 and P == 0 and V == 0:
        break
    day_1 = V // P * L
    if L > V % P:
        day_2 = V % P
    else:
        day_2 = L
    print(f'Case {idx}: {day_1 + day_2}')
    idx += 1