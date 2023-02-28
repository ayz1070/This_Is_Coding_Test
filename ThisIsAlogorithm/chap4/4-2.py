# 1시나 2시나 3이 포함된 시간의 수는 같다.
# 3의 배수 시만 예외지
# 01시 00분 00초 부터 01시 59분 59초까지의 3의 갯수는?
# 1분 사이에 3이 포함된 경우는 5+  

n=int(input())
count =0 
for h in range(0,n+1):
    for m in range(0,60):
        for s in range(0,60):
            if h%10 ==3 or h//10 == 3 or m%10==3 or s%10==3 or m//10 ==3 or s//10 == 3:
                count+=1

print(count)
