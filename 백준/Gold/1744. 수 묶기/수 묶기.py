nums = []
n_nums = []
p_nums = []
m_nums = []

for _ in range(int(input())):
    num = int(input())
    if num < 0:
        n_nums.append(num)
    elif num > 1:
        p_nums.append(num)
    else:
        m_nums.append(num)

n_nums = sorted(n_nums, reverse=True)
p_nums = sorted(p_nums)

final = m_nums.count(1)

if len(p_nums) % 2 == 1:
    final += p_nums[0]
    
if 0 not in m_nums and len(n_nums) % 2 == 1:
    final += n_nums[0]
    
for idx in range(len(p_nums)-1, 0, -2):
    final += (p_nums[idx] * p_nums[idx-1])

for idx in range(len(n_nums)-1, 0, -2):
    final += (n_nums[idx] * n_nums[idx-1])
    
print(final)