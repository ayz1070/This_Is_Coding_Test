from bisect import bisect_left,bisect_right

arr = [1,2,2,2,3,3,3,3,3,3,5,6,7]

# 왼쪽에서 부터 3의 인덱스를 찾기
print(bisect_left(arr,3))

# 오른쪽에서 부터 3의 인덱스를 찾기
print(bisect_right(arr,3))