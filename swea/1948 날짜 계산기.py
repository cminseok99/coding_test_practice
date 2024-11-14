T = int(input())  
month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
for test_case in range(1, T + 1):
    arr=list(map(int, input().split()))
    ans=0

    if arr[0]==arr[2]:
        ans= arr[3]-arr[1]+1
        print(f'#{test_case} {ans}')
    elif arr[1]<=arr[3]:
        for k,v in month_days.items():
            if arr[0] <= k <= arr[2]-1:
                ans+=v
        ans=ans+arr[3]-arr[1]+1
        print(f'#{test_case} {ans}')

    else:
        for k,v in month_days.items():
            if arr[0] <= k <= arr[2]-1:
                ans+=v
        ans=ans-(arr[1]-arr[3]-1)
        print(f'#{test_case} {ans}')






    
    










    
     


    








    

    


    

















