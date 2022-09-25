# 내적

def solution(a, b):
    answerList = []
    for i in range(len(a)):
        answerList.append(a[i]*b[i])
    answer = sum(answerList)
    return answer
