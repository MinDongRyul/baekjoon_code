import sys
input = sys.stdin.readline

def func(n : int, m : int):
    dic = {} 
    for _ in range(n+m):
        name = input().rstrip()
        if name not in dic:
            dic[name] = 1
        elif name in dic:
            dic[name] += 1
    
    dic = dict(sorted(dic.items()))
            
    temp = []
    count = 0
    for key, val in dic.items():
        if val >= 2:
            temp.append(key)
            count += 1

    print(count)
    for name in temp:
        print(name)
        
N, M = map(int, input().split())
func(N, M)
