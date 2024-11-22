def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    
    
    
    for i in range(len(arr1)): 
        for j in range(len(arr2[0])): #이 부분을 이렇게짠이유는 오른쪽행렬의 각행의 원소의 갯수에 따라 증가혹은 감소해주기 위해서이다(3행 2열이면 len(arr2[0])가 3이됨(행렬의 곱성질때문))
            for x in range(len(arr2)):
                answer[i][j]+=arr1[i][x]*arr2[x][j]
            

    return answer


#2차원 배열상에서 반복문 i j x 조합하여 가지고 노는 문제

#나는 테스트케이스만 통과하였는데, 내 코드 x를 보면 arr2의 길이에따라 곱해지는 갯수가 달라지는데 나는 range(len(arr2[0]))로 하였다
#이렇게하면 안되는 이유는 행렬곱을 할때오른쪽행렬은 열로내려가며 곱하기 때문에 행쪽 원소를 반복시키면 안되고 열쪽원소가 늘어나면 그거에 맞추어 반복해줘야하기때문에 오류가 발생한 것이다.

#빡구현까진 아니지만 생각을 어느정도 해야하는 문제 다시 풀어봐야할 문제