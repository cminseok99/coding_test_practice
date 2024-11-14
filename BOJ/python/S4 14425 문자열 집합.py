N, M = map(int, input().split())
k=0
S=[]

for i in range(N):
    data = input()
    S.append(data)

for j in range(M):
    data1 = input()
    if data1 in S:
        k+=1

print(k)