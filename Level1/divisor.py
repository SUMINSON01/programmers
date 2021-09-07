# 약수의 개수와 덧셈

def divisor(num): # 약수 갯수 구하기
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count % 2 == 0:
        return True
    else:
        return False

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if divisor(i):
            answer += i
        else:
            answer -= i
        #if int(sqrt) == sqrt: # 제곱근이 정수일 경우 약수가 홀수
        #    answer -= i
        #else:
        #    answer += i
    return answer
