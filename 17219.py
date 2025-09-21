import sys
n,m=map(int,input().split())
ed=dict()
for i in range(n):
    com=sys.stdin.readline()
    com=com.split()
    ed[com[0]]=com[1]
for i in range(m):
    site=sys.stdin.readline()
    site=site.strip()
  
    print(ed[site])
