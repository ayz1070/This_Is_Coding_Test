# 이런 문제는 문자열을 하나하나 방문하면서 확인한다.
# 숫자면 합계, 알파벳이면 별도의 리스트에 저장

data =input()
result =[]
value =0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))

# isapha 함수는 알파벳인지 확인해주는 함수
# 문자 리스트도 sort 가능
# ''.join(result)로 리스트를 벗길 수 있다!!