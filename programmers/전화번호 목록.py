def solution(phone_book):
    hash_map ={}
    
    for phone_number in phone_book:
        hash_map[phone_number] =1
        
    for phone_number in phone_book: # ["6","12","6789"]중에서 "6","12","6789" 뽑아
        jubdo =""
        for number in phone_number: # "6","12","6789" 중 6 , 1, 2, 6, 7, 8,9 ..뽑아
            jubdo+=number
            if jubdo in hash_map and jubdo != phone_number:
                return False
    return True
            
    
    
