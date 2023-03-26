# n은 행, m은 열
n,m=map(int,input().split())

arr = list()
for _ in range(n):
    arr.append(min(list(map(int,input().split()))))
    
print(max(arr))
