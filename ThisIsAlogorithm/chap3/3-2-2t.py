n,m,k = map(int,input().split())

nums = list(map(int,input().split()))

nums.sort(reverse= True)

# 6+6+6+5 를 한 세트(s)라고 설정. 여기서는 m은 8, k는 3이기 때문에 2세트가 존재함
s = m//(k+1)

# (6*3  + 5) 는 4칸 짜리 한 세트에 들어갈 수 있는 최대값
result = s*(nums[0]*k + nums[1]) + m%(k+1) *nums[0]
print(result)

