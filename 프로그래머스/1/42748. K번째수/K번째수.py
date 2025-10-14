def prep(elements, array):
    i = elements[0]
    j = elements[1]
    k = elements[2]
    
    if len(array) == 1:
        return array[0]
    else:
        prep1 = array[i-1:j]
        prep2 = sorted(prep1)[k-1]
    
    return prep2
    
def solution(array, commands):
    answer = []
    for i in commands:
        answer.append(prep(i, array))
    return answer