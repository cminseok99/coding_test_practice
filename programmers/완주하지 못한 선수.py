def solution(participant, completion):
    hash_dict ={}
    sumhash = 0
    for i in participant:
        hash_dict[i]= hash(i)
        sumhash = sumhash+hash(i)
    for j in completion:
        sumhash = sumhash-hash(j)
    return hash_dict[sumhash]