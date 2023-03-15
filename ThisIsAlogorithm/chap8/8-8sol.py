n,m = map(int,input().split())

# 화폐들 입력 받는다 ㅇㅋ
coins =[]
for i in range(n):
    coins.append(int(input()))

# 초기화한다. ㅇㅋ
d = [10001]*(m+1)

# 어떤 화폐단위여도 0원을 만드는 것은 0개의 코인 ㅇㅋ
d[0] = 0

# 점화식 -> a_{i} = min(a_{k}, a_{i-k} + 1)
for i in range(n):
    # coins[i] 부터 하는 것은 이전 값들로 하면 인덱스가 음수가 되잖아 의미가 없다는 거지
    for j in range(coins[i],m+1):
        # a_{i-k}를 만드는 방법이 존재한다면... 점화식을 활용할 수 있다.
        if d[j-coins[i]] != 10001:
            d[j] = min(d[j],d[j-coins[i]]+1)    # 점화식

if d[m] == 10001:
    print(-1)
else:
    print(d[m])