T=int(input())

for i in range(T):
    a=int(input())
    des=0
    cnt=0
    for k in range(1,10):
        x=0
        y=0
        x=k
        y=a//k
        if x<10 and y<10 and a%k==0:
            cnt+=1
        else:
            des+=1

    if cnt>=1:
        print("#%d Yes" %(i+1))
    else:
        print("#%d No" %(i+1))
    
    
