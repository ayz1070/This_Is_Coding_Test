# 이 문제는 빨리 끝나는 강의로 선택하는게 이득!
n = int(input())

times = list()
for _ in range(n):
    start,end = map(int,input().split())
    times.append([start,end])

# 일단 시작 시간 순으로 정렬
times = sorted(times, key=lambda a: a[0])
# 시작 시간 순으로 정렬된 것을 끝나는 시간으로 또 정렬
times = sorted(times,key=lambda x:x[1])

end_time = 0
# schedule = list()
# 우리가 필요한 것은 리스트가 아니라 갯수니까 조금 더 줄여보자!
count = 0

for i,j in times:
    if i >= end_time:
        # schedule.append([i,j])
        count += 1
        end_time = j

print(count)