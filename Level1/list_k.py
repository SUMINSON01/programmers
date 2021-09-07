# K번째 수

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        slic = array[commands[i][0]-1:commands[i][1]]
        sortslic = sorted(slic)
        sortslic2 = sortslic[commands[i][2]-1]
        answer.append(int(sortslic2))
    return answer
