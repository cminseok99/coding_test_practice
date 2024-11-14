# 윈도우 슬라이딩 문제

T = int(input())

for i in range(0, T) : 
    
    NM = input()

    A = input().split() 
    A = list(map(int, A)) # 배열의 모든 값을 정수형(int)로 변환한 list 생성
    B = input().split() 
    B = list(map(int, B))

    # B열의 길이가 더 짧을 경우, A와 B swap (이렇게 하면 항상 B열의 길이가 더 길다.)
    if len(A) > len(B) :
        B, A = A, B

    arr = []

    for k in range(len(B)-len(A)+1) : 
        sum = 0
        for r in range(len(A)) : 
            sum += A[r] * B[r+k]
        arr.append(sum)  

    print(f'#{i+1} {max(arr)}')