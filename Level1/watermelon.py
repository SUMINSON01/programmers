# 수박수박수박수박수박수?

def watermelon(n):
    answer=''

    for i in range(n):
        if(i%2==0):
            answer+='수'
        if(i%2==1):
            answer+='박'
    return answer
