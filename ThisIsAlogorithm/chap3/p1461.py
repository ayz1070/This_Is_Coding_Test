n,m = map(int,input().split())

# 책의 위치
book = list(map(int,input().split()))

pos = list()
neg = list()

# 양수, 음수 분리
for i in book:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)

# 절대값이 큰 순으로 내림차순 정렬
pos.sort(reverse=True)
neg.sort()

# -39 -37 -29 -28 -6 이 있으면 -39, -29, -6 저장
neg_walks = list()
for i in range(0,len(neg),m):
    neg_walks.append(neg[i])

# 11 2 있으면 11 저장
pos_walks = list()
for i in range(0,len(pos),m):
    pos_walks.append(pos[i])

# 최상위 조건은 예제 입력 4를 고려함
if len(neg_walks) != 0 and len(pos_walks) !=0:
    # 최소 걸음이기 때문에 절대값이 큰 걸음수를 한 번 곱하는 것이 이득!
    if abs(neg_walks[0]) > pos_walks[0]:
        # 음수 집합의 최대 걸음수가 더 크면 
        result = abs(2*sum(neg_walks)) - abs(neg_walks[0]) + 2*sum(pos_walks)
    else:
        # 양수 집합의 최대 걸음수가 더 크면
        result = 2*sum(pos_walks) - pos_walks[0] + 2*abs(sum(neg_walks))
else:
    # 예제 입력 4를 고려함
    result = abs(book[0])

print(result)

# 테스트는 다 맞는데..
# 뭘 놓치고 있는걸까요...???
# 전부 음수일 때 고려하자