# 핸드폰 번호 가리기

def hideNumbers(phone_number):
    answer = (len(phone_number)-4) * "*"
    answer += phone_number[-4:]
    return answer
