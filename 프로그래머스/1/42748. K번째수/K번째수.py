# i ~ j 번째까지 자르기 , 정렬하기, k번째 숫자 찾기
# commands가 2차원 배열
def solution(array, commands):
    answer = []
    for command in commands:
        answer.append(sorted(array[command[0]-1 : command[1]])[command[2]-1])
    return answer