import sys
input = sys.stdin.readline

def func(n : int, m : int):
    total_value = 0
    total_lst = []
    
    dic = {}
    
    # n_lst = [input() for _ in range(n+m)]
    #　m_lst = [input() for _ in range(m)][1:]
    
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

    return count, temp
        
N, M = map(int, input().split())
value, lst = func(N, M)
print(value)
for name in lst:
    print(name)