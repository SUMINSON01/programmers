# 정수 제곱근 판별

import math

def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return int(math.sqrt(n)+1)**2
    else:
        return -1
