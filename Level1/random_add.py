# 두 개 뽑아서 더하기

from itertools import combinations

def solution(numbers):
    answer = set()
    for arr in list(combinations(numbers, 2)):
        answer.add(sum(arr))
    return sorted(answer)
