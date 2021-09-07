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
