def solution(arr):
    arr2=[]
    for i in range(len(arr)):
        if [arr[i]] != arr[i+1 : i+2]: #배열 슬라이싱: [값] 형대, arr[i]는 숫자이므로 비교해주려면 []> 배열로 감싸줘야한다
            arr2.append(arr[i])
    return arr2
        
     
        
        
    
    