while True:
    x, y, z = map(int, input().split())
    if x == 0 & y == 0 & z == 0:
        break
    side_lengths = sorted([x, y, z], reverse=True)
    
    if len(set(side_lengths)) == 1:
        print('Equilateral')
    elif len(set(side_lengths)) == 2 and (side_lengths[0] == side_lengths[1] or side_lengths[0] < side_lengths[1] + side_lengths[2]):
        print('Isosceles')
    elif side_lengths[0] < side_lengths[1] + side_lengths[2]:
        print('Scalene')
    else:
        print('Invalid')