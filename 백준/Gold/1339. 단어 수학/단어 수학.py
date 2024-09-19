w, final_w = {}, {}
total = 0
lst = [input() for _ in range(int(input()))]

for value in lst:
    for idx, val in enumerate(value[::-1]):
        if val not in w:
            w[val] = 10 ** idx
        else:
            w[val] += 10 ** idx

w = sorted(w.items(), key=lambda x : x[1], reverse=True)

for idx, item in enumerate(w):
    final_w[item[0]] = str(9 - idx)

for value in lst:
    for key in final_w:
        value = value.replace(key, final_w[key])
    total += int(value)
    
print(total)