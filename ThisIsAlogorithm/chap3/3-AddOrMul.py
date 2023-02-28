s=input()

result = int(s[0])

for i in range(1,len(s)):
    if(int(s[i])==0 or int(s[i]) == 1 or result*int(s[i])>2000000000):
        result += int(s[i])
    else:
        result *= int(s[i])
    print(result)

print(result)
