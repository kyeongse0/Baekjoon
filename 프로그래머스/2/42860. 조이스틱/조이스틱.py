# 아스키 코드?
# 최소가 어렵다,,,
def solution(name):
    answer = 0
    a = len(name)*"A"
    
    for i in name:
        up = ord(i) - ord("A")
        down = ord('Z') - ord(i) + 1
        answer += min(up,down)
            
    move = len(name) - 1    # 기본값
    for i in range(len(name)):
        next_idx = i +1
        while next_idx < len(name) and name[next_idx] =='A':
            next_idx += 1
        move = min(move, 2*i+ len(name) - next_idx, 2*(len(name)-next_idx)+i)

    answer += move
    return answer