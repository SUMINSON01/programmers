# 소수 만들기

from itertools import combinations

# 소수임을 판별
def isPrimeNumber(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, num//2 + 1):
            if num % i == 0:
                return False
        return True

def solution(nums):
    answer = 0
    cmb = list(combinations(nums, 3)) # nums배열을 3개씩 조합 후 list로 변경
    for arr in cmb:
        if isPrimeNumber(sum(arr)):
            answer += 1
    return answer
