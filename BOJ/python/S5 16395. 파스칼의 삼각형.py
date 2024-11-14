a,b =map(int,input().split())
arr=[[0]*32 for _ in range(32)]
arr[0][1]=1

for i in range(1,31):
    for j in range(1,i+2):

        arr[i][j]=arr[i-1][j-1]+arr[i-1][j]


print(arr[a-1][b])







