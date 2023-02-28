words = input()

# 문자열과 정수가 섞여 있네 어떻게 처리할까?
# 하나씩 방문하고 일단 문자와 정수를 분리해볼까?
sentence=[]
num = []
sen =""
for word in words:
    if ord('A')<=ord(word)<=ord('Z'):
        sentence.append(word)
    else:
        num.append(int(word))
    

for i in sorted(sentence):
    sen += i

print(sen+str(sum(num)))