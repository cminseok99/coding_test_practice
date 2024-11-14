T = int(input())

for test_case in range(1, T + 1):
    
    b, c = map(int, input().split())
    arr_s=['D0','C-','C0','C+','B-','B0','B+','A-','A0','A+']
    
    arr_a=[]
    for i in range(b):
        arr1=list(map(int,input().split()))
        score=arr1[0]*0.35+arr1[1]*0.45+arr1[2]*0.2
        arr_a.append(score)
        
    s= arr_a[c-1]
    arr_a.sort()
    e=0
    
    for k in range(10):
        for j in range(e,e+b//10):
            if s==arr_a[j]:
                print(f'#{test_case} {arr_s[k]}')
        if k<10:   
            e+=b//10 
            
        


   




    
    
    
    



                    
 
   



    
    










    
     


    








    

    


    

















