import heapq as hq

n = int(input())
cards = list()

for _ in range(n):
    hq.heappush(cards,int(input()))

result = 0

while len(cards)>1:
    plus = hq.heappop(cards) + hq.heappop(cards)
    result += plus
    hq.heappush(cards,plus)

print(result)