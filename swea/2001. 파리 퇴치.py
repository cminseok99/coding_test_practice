T = int(input())

for test_case in range(1, T + 1):
    n,m =map(int,input().split())
    arr= [list(map(int, input().split())) for _ in range(n)]
    ans_arr=[]

    for i in range(n-m+1):  #밑으로 내려가면서
        
        for j in range(n-m+1): #옆으로 넘어가면서
            cnt=0



            for x in range(i,m+i):   # m=2일때에는 이걸 이용하여 4개를 더해야함 2 2이런식으로(i와 j활용)

                for y in range(j,m+j):
                    cnt+=arr[x][y]

            ans_arr.append(cnt)


    print(f'#{test_case} {max(ans_arr)}')



#구현 문제 팁 : 반복문에서 반복해야 할 것 구도를 먼저 잡는다. 중첩반복문에서 특히 이전 for 뒤 변수들을 활용하여 코드는 짜는 연습 









