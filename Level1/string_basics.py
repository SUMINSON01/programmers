# 문자열 다루기 기본

def solution(s):
    try:
        n = len(s)
        s = int(s)
        if n == 4 or n == 6 and type(s) == 'int':
            return True
        else:
            return False
    except:
        return False
