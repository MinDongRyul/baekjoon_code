import heapq
import sys

input = sys.stdin.readline
n=int(input())
front=[]
back=[]

mid=int(input())
print(mid)

for i in range(2, n+1):
    k=int(input())

    if k<mid:
        heapq.heappush(front, -k)
        if i%2==0:
            heapq.heappush(back, mid)
            mid=-heapq.heappop(front)
    else:
        heapq.heappush(back, k)
        if i%2==1:
            heapq.heappush(front, -mid)
            mid=heapq.heappop(back)

    print(mid)