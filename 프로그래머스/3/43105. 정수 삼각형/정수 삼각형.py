# 자기 인덱스랑 그 다음 인덱스로만 움직일 수 있음
# triangle의 다음 리스트에서 내 인덱스와 그 다음 인덱스만을 살핌
# 결국 반복이 필요? -> 함수 정의가 필요?
def solution(triangle):

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:      # 맨 왼쪽
                triangle[i][j] += triangle[i-1][j]
            elif j == i:    # 맨 오른쪽
                triangle[i][j] += triangle[i-1][j-1]
            else:           # 가운데
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1])