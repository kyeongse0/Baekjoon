# start, end를 구분해두고 특정 기준에 의해 설치?
# 특정 기준은 뭘까...
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    cam = -30001   # 카메라 위치 (문제에서 최소 위치가 -30000이니까 그보다 작게)
    
    for start, end in routes:
        # 현재 카메라로 이 차를 못 찍을 때만 새로 설치
        if start > cam:
            answer += 1
            cam = end   # 이 차의 끝 지점에 설치
    return answer