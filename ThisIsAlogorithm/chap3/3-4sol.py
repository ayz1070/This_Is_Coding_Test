n,k = map(int,input().split())

result = 0

while(True):
    target = (n//k) * k # 몫 * k 니까 나누어 떨어지는 숫자를 찾은거지
    # 나누어 떨어지는 숫자까지의 1을 뺀 횟수를 더한다!
    result += n-target
    n = target
    if n<k:
        break
    n//=k

result += (n-1)
print(result)