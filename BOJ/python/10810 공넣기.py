N, M= map(int, input().split())

box=[0]*N

for b in range(M):
    i, j,k= map(int, input().split())
    for a in range(i,j+1):
        box[a-1] =k

for i in range(N):
    print(box[i], end=' ')
