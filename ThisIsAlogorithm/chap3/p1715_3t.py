from heapq import heappush,heappop

cards = list()

result = 0
total = 0

n = int(input())


for _ in range(n):
    heappush(cards,int(input()))
    
while(len(cards)>1):
    total = heappop(cards) + heappop(cards)
    result += total
    heappush(cards,total)
print(result)