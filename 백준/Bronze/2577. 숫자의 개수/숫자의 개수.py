num = 1
dict_ = {}
for idx in range(10):
    dict_[str(idx)] = 0

for _ in range(3):
    num *= int(input())

for num_ in str(num):
    dict_[num_] += 1

for key in dict_:
    print(dict_[key])