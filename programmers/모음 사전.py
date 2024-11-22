###1.원리 이해 후 식 도출해서 코드 구현

###2.파이썬 라이브러리 활용 (중복조합)###
from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    words.sort()
    return words.index(word) + 1
