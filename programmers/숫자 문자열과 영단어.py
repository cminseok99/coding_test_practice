def solution(s):
    dict = {'zero':'0','one':'1','two':'2', 'three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    str_s = ''
    temp =''
    ex_str='0123456789'
    for i in s:
        if i in ex_str:
            str_s+=i
        else:
            temp+=i
            if temp in dict:
                str_s+=dict[temp]
                temp=''  
    return int(str_s)
