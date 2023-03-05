n,x = map(int,input().split())

arr = list(map(int,input().split()))

if(x in arr):
    print(arr.count(x))
else:
    print(-1)
