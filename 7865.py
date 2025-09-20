n=int(input())
people=list()
rank=list()
for i in range(n):
    temp=list(map(int,input().split()))
    people.append(temp)


for i in range(n):
    k=1
    for j in range(n):
        if i == j:
            continue
        if people[i][0]<people[j][0] and people[i][1]<people[j][1]:
            k+=1
    rank.append(k)
result=""
for i in range(n):
    result+=str(rank[i])+" "
print(result)
