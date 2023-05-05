# 앞 두 숫자를 더한 것을 무조건 다음 턴에 비교한다는 보장이 없구나!!


import heapq

cards = list()

result = 0

n = int(input())

if n > 1:
    for _ in range(n):
        heapq.heappush(cards,int(input()))

    result =0
    min_value = cards[0]

    for i in range(0,n):
        result += (n-i) * heapq.heappop(cards)

    result -= min_value
    print(result)
else:
    print(0)
