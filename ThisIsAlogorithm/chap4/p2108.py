n=int(input())
nums = list()
for i in range(n):
    nums.append(int(input()))

# 산술 평균
# round는 반올림
print(round(sum(nums)/n))

# 중앙값
nums.sort()
print(nums[n//2])

# 최빈값
count_num = list()
for i in nums:
    count_num.append(nums.count(i))
dic = {}

# 정렬된 입력값과 그 갯수를 딕셔너리로 매핑
j=0
for i in nums:
    dic[i] = count_num[j]
    j+=1

# 
max_dict = max(dic.values())
choibin = list() 
for i in dic.keys():
    if dic[i] == max_dict:
        choibin.append(i)
choibin.sort()
# 튜플 형태로 반환됨
sorted_dict = sorted(dic.items(), key=lambda x : x[1])
# 예제 2처럼 인덱스가 하나일 경우 생각해야 함
if n> 1:
    # 최빈값이 중복이 있는 경우
    if sorted_dict[len(sorted_dict)-1][1] == sorted_dict[len(sorted_dict)-2][1]:
        print(choibin[1])
    # 최빈값이 중복이 없는 경우
    else:
        # values로 정렬된 튜플에서 values가 가장 큰 key를 구하면 된다. 
        print(sorted_dict[len(sorted_dict)-1][0])
else:
    print(nums[0])

# 범위
if n>1:
    # 부호가 다르면
    if (nums[0]>0 and nums[n-1]<0) or (nums[0]<0 and nums[n-1]>0):
        print(abs(nums[0]) + abs(nums[n-1]))
    else:
    # 부호가 같으면
        print(abs(nums[0] - nums[n-1]))

else:
    print(0)