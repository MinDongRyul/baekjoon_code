def generate_map(n, m):
    map_ = [list(map(int, input().split())) for _ in range(n)]    
    return map_
    
def initialize_dice():
    dice = [[-1, 0, -1],
            [0,  0,  0],
            [-1, 0, -1],
            [-1, 0, -1]]
    return dice
    
def roll_dice(to_mv_loc, dice):
    if to_mv_loc == 4:
        dice[2][1], dice[3][1], dice[0][1], dice[1][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
    elif to_mv_loc == 3:
        dice[2][1], dice[3][1], dice[0][1], dice[1][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
    elif to_mv_loc == 2:
        dice[1][0], dice[3][1], dice[1][2], dice[1][1] = dice[1][1], dice[1][0], dice[3][1], dice[1][2]
    else:
        dice[1][1], dice[1][0], dice[3][1], dice[1][2] = dice[1][0], dice[3][1], dice[1][2], dice[1][1]
    return dice
        
def check_map(map_, x, y, to_mv_loc, dice):
    
    dice = roll_dice(to_mv_loc, dice)
    current_map_value = map_[x][y]
        
    if current_map_value == 0:
        map_[x][y] = dice[3][1]
    else:
        dice[3][1] = current_map_value
        map_[x][y] = 0
    
    print(dice[1][1])
    return map_, dice
    
def move_dice(map_, n, m, x, y, k, dice):
    to_mv_cnt = list(map(int, input().split()))
    for to_mv_loc in to_mv_cnt:
        if to_mv_loc == 4:
            x += 1
            if x >= n:
                x -= 1
                continue
        elif to_mv_loc == 3:
            x -= 1
            if x < 0:
                x += 1
                continue
        elif to_mv_loc == 2:
            y -= 1
            if y < 0:
                y += 1
                continue
        else:
            y += 1
            if y >= m:
                y -= 1
                continue
        map_, dice = check_map(map_, x, y, to_mv_loc, dice)
    
n, m, x, y, k = map(int, input().split())
map_ = generate_map(n, m)
dice = initialize_dice()
move_dice(map_, n, m, x, y, k, dice)