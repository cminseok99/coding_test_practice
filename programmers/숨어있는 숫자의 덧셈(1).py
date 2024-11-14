def solution(my_string):
    str_e = '1234567890'
    answer = ''
    for i in my_string:
        if i in str_e:
            answer+=i
            
    return sum(int(j) for j in answer)