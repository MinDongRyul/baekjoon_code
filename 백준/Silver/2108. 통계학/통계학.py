import sys
input = sys.stdin.readline

class agg:
    def __init__(self, N, nums):
        self.N = N
        self.nums = nums
        
    def mean(self):
        return round(sum(self.nums) / self.N)

    def median(self):
        return self.nums[self.N//2]

    def mode(self):
        num_dict = {}
        for num in self.nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        num_dict = sorted(num_dict.items(), key=lambda x : x[1], reverse=True)
        
        if len(self.nums) == 1:
            return self.nums[0]
        elif self.N == len(set(self.nums)):
            return self.nums[1]
        else:
            if num_dict[0][1] == num_dict[1][1]:
                return num_dict[1][0]
            elif num_dict[0][1] > num_dict[1][1]:
                return num_dict[0][0]
        
    def max_min(self):
        return max(self.nums) - min(self.nums)
    
N = int(input())
nums = sorted([int(input())for _ in range(N)])
answer = agg(N, nums)

print(answer.mean())
print(answer.median())
print(answer.mode())
print(answer.max_min())