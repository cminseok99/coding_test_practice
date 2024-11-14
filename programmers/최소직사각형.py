
        
def solution(sizes):
    a=[]
    for x in sizes:
        a.append(max(x))
    b=max(a)
    
    
            
    arr3=[]
    for size in sizes: 
        if size[0] > size[1]:
            arr3.append(size[1])
        elif size[0] <= size[1]:
            arr3.append(size[0])
        c = max(arr3)
        
    return b*c