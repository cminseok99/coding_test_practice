t = 10

for j in range(1, t + 1):
    n=int(input())
    arr= [list(map(int, input().split())) for _ in range(100)]
    cnt3=0
    cnt4=0

    ans_arr=[]

    for i in range(100):
        cnt=0
        cnt2=0
        for k in range(100):
            cnt+=arr[i][k]
            cnt2+=arr[k][i]

        ans_arr.append(cnt)
        ans_arr.append(cnt2)  

    for x in range(100):
        cnt3+=arr[x][x]
        cnt4+=arr[x][99-x]

    ans_arr.append(cnt3)
    ans_arr.append(cnt4)

    print(f'#{j} {max(ans_arr)}')



    


        
   




      


            
