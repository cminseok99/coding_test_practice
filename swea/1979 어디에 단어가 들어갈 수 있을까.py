T = int(input())  

for test_case in range(1, T + 1):
    a, b = map(int, input().split())  
    arr = [list(map(int, input().split())) for _ in range(a)]

    res4 = 0
    res3 = 0

    # 행을 기준으로 연속된 1의 개수 계산
    for i in range(a):
        cnt1 = 0
        for j in range(a):
            if arr[i][j] == 1:
                cnt1 += 1
            else:
                if cnt1 == b:
                    res4 += 1  # 연속된 1이 b 개일 경우 증가 (1 0 혹은 111 0 등 0이 등장하였을 때)
                cnt1 = 0
        if cnt1 == b:  # 마지막에 연속된 1이 b 개일 경우 처리 (i 한 싸이클 끝났을 때(j가 다 돌았을 때))  
            
            res4 += 1

    # 열을 기준으로 연속된 1의 개수 계산
    for k in range(a):
        cnt2 = 0
        for m in range(a):
            if arr[m][k] == 1:
                cnt2 += 1
            else:
                if cnt2 == b:
                    res3 += 1  # 연속된 1이 b 개일 경우 증가
                cnt2 = 0
        if cnt2 == b:  # 마지막에 연속된 1이 b 개일 경우 처리
            res3 += 1

    print(f'#{test_case} {res4 + res3}')
