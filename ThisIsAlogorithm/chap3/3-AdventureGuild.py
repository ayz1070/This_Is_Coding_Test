# 2 3 1 2 2
# 1 2 2 2 3
# 1/ 2 2 / 2 3 마지막 버림
n=int(input())

gong = list(map(int,input().split()))

gong.sort()

count =0
i = 0
while(True):
    i += gong[i]
    if i >= n:
        break
    count +=1 

print(count)