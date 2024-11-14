T=int(input())

for i in range(T):

    arr=list(map(int, input().split()))
    a=arr[0]+arr[2]
    b=arr[1]+arr[3]

    if b>60 and a>=12:
        a=a+1-12
        b=b-60
        print("#%d %d %d" %(i+1,a,b))
    elif b>60 and a<12:
        a=a+1
        b=b-60
        print("#%d %d %d" %(i+1,a,b))

    elif b<60 and a<12:
        print("#%d %d %d" %(i+1,a,b))

    elif arr[1]+arr[3]<60 and a>=12:
        a=a-12
        print("#%d %d %d" %(i+1,a,b))