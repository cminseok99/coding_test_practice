t=int(input())

for j in range(t):
    str_in=input()
    basic_str='0'*len(str_in)
    str_in=list(str_in)
    basic_str=list(basic_str)
    cnt=0
    for i in range(len(str_in)):
        if str_in[i] != basic_str[i]:
            cnt+=1
            for k in range(i,len(str_in)):
                basic_str[k]=str_in[i]
    print("#%d %d" %(j+1,cnt))

        