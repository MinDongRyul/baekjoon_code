num = 1    
for _ in range(3):
    num *= int(input())
    
num = list(map(int, str(num)))
    
for num_ in range(0, 10):
    print(num.count(num_))