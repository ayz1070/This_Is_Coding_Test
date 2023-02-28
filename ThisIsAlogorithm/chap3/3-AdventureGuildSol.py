n=int(input())

gong = list(map(int,input().split()))

gong.sort()

count =0
result = 0

for i in gong:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)