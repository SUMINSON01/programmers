# 두 정수 사이의 합

def adder(a, b):
    answer=0
    if a==b:
        return a;
    if a<b:
        temp=a
        a = b
        b = temp

    while(True):
        answer+=a
        a-=1
        if a==b:
            answer+=a
            return answer
