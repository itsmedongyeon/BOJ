condo=list()
n=int(input())
for i in range(n):
    room=input()
    condo.append(room)
rowcnt=0
colcnt=0
for i in range(n):
    cnt=0
    for j in range(n):
        if condo[i][j]==".":
            cnt+=1
        if condo[i][j]=="X":
            if cnt>=2:
                rowcnt+=1
                cnt=0
            else:
                cnt=0
        if j==n-1:
            if cnt>=2:
                rowcnt+=1


for i in range(n):
    cnt=0
    for j in range(n):
        if condo[j][i]==".":
            cnt+=1
        if condo[j][i]=="X":
            if cnt>=2:
                colcnt+=1
                cnt=0
            else:
                cnt=0
        if j==n-1:
            if cnt>=2:
                colcnt+=1

print(rowcnt,colcnt)
