# 틀림 조금 더 고려해보자!

n = int(input())
cards = list()
for _ in range(n):
    cards.append(int(input()))

cards.sort()
result = - cards[0]

for i in range(0,n):
    result += cards[i] * (n- i)

print(result)