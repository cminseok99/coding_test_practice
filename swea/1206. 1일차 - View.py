t = 10

for j in range(1, t + 1):

    n= int(input())
    arr = list(map(int, input().split()))  
    cnt=0
    
    for i in range(2,len(arr)):

        if arr[i-2]<arr[i] and arr[i-1]<arr[i] and arr[i+1]<arr[i] and arr[i+2]<arr[i]:
            cnt+=arr[i]-max(arr[i-2],arr[i-1],arr[i+1],arr[i+2])



    print(f'#{j} {cnt}')



    


    
