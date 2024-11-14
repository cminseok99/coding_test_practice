a = int(input())
for i in range(a):
    n=int(input())
    arr= list(map(int, input().split()))
    cnt=[0]*101
    for j in range(len(arr)):
        cnt[arr[j]]+=1
    arr2=[]
    max_count = max(cnt)
    for k in range(len(cnt)):
        if cnt[k]==max_count:
            arr2.append(k)
    h=max(arr2)
    print("#%d %d"%(n,h))



