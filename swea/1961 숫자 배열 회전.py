T = int(input())  

for test_case in range(1, T + 1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    ans_arr=[[]*3 for _ in range(3)]
    

    
    for i in range(n): 
        res=''
        for j in range(n):
            res+=str(arr[n-1-j][i])
        ans_arr[0].append(res)
        

    for i in range(n): 
        
        res=''
        for j in range(n):
            res+=str(arr[n-1-i][n-1-j])

        ans_arr[1].append(res)


    for i in range(n): 
        res=''
        for j in range(n):
            res+=str(arr[j][n-1-i])

        ans_arr[2].append(res)

    print(f'#{test_case}')
    for w in range(n):
        print(ans_arr[0][w],ans_arr[1][w],ans_arr[2][w])

    

   






    
    










    
     


    








    

    


    

















