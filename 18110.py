import math
import sys
def ROUND(num):#파이썬 내장 round 함수는 오사오입방식사용 짝수쪽으로 반올림 오차발생으로 인해 round함수를 직접만들어줌
    if num%1 >=0.5:
        return math.ceil(num)
    else:
        return math.floor(num)


n=int(input())
rm=ROUND(n*0.15)
ranks=list()
result=0
for i in range(n):
    rank=int(sys.stdin.readline())#반복문이 늘어날수록 입력받는데 시간이 오래걸려서 입력이 빠른 sys.stdin.readlint()을 만들어줌
    ranks.append(rank)
ranks.sort()

for i in range(rm,n-rm):
    result+=ranks[i]
if(n==0):
    print("0")
else:
    print(ROUND(result/(n-2*rm)))
