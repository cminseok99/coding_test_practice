t=int(input())

for i in range(1,t+1):
    n=int(input())
    arr=[list(map(int,input())) for _ in range(n)]
    

    s=n//2
    e=s+1
    res=0

    

    for j in range(n):
        for k in range(s,e):
            res+=arr[j][k]

        if j<n//2:
            s-=1
            e+=1

        else:
            s+=1
            e-=1

    print(f'#{i} {res}')




