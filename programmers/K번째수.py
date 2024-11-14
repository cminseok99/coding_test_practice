def solution(array, commands):
    ans=[]
    for nums2 in commands:
        
            a=array[nums2[0]-1:nums2[1]]
            a.sort()
            ans.append(a[nums2[2]-1])
    return ans 

    
    
    
    