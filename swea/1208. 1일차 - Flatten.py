t = 10

for i in range(1, t + 1):
    m = int(input())  
    arr = list(map(int, input().split()))  
    
    cnt = 0

    while m > 0: #조정횟수 사라질때까지 반복
        max_val = max(arr) 
        min_val = min(arr)  

        
        if max_val - min_val <= 1:  #조정횟수 끝나기전 평탄화끝나면 브레이크로 반복문 탈출
            break

       # 최대 최소 인덱스를 찾아놓기
        max_idx = arr.index(max_val)    
        min_idx = arr.index(min_val)

        
        arr[max_idx] -= 1
        arr[min_idx] += 1

        m -= 1 
        
        #다시 조건 검사로 올라가면 max 값 min값 새로(다시) 찾아주고~

   
    cnt = max(arr) - min(arr)
    print(f'#{i} {cnt}')
