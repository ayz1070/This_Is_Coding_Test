n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
C = sorted(B,reverse=True)

result = list()
for _ in range(n):
    result.append(A.pop()*C.pop())

print(sum(result))

