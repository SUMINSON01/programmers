# 키패드 누르기

def keypad(num, hand):
    left = 10
    right = 12
    answer=''

    for i in num:
        if i == 1 or i == 4 or i == 7:
            answer+='L'
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer+='R'
            right = i
        else:
            if i==0:
                i=11
            leftDis = abs(left-i)//3+abs(left-i)%3
            rightDis = abs(right-i)//3+abs(right-i)%3

            if leftDis > rightDis:
                answer+='R'
                right = i
            elif leftDis < rightDis:
                answer+='L'
                left = i
            else:
                if hand == 'right':
                    answer+='R'
                    right = i
                elif hand == 'left':
                    answer+='L'
                    left = i

    return answer
