loc = input()

column = ord(loc[0])-ord('a') +1
row = int(loc[1])

count = 0
# uur,uul,urr,ull,ddr,ddl,drr,dll
steps = [(-2,1),(-2,-1),(-1,2),(-1,-2),(2,1),(2,-1),(1,2),(1,-2)]

for step in steps:
    next_row = row+step[0]
    next_column = column+step[1]
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        count+=1
print(count)