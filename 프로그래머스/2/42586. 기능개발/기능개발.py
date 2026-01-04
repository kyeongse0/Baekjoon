# 작업[i] + 속도[i] * 날짜가 100 이상이 되는 날 배포 가능하다
# 각 배포마다 몇 개의 기능이 배포되는가?
# 스택 or 큐?
def solution(progresses, speeds):
    answer = []
    days = []       # 기능 개발 완료되는 날 리스트
    for i in range(len(speeds)):
        num = 0
        while progresses[i] + speeds[i]*num < 100:  # 100 되기 전까진 도는 루프
            num += 1
        days.append(num)    # 100을 넘은 값의 num 저장
        
    current = days[0]       # 첫 배포 서비스 기준
    cnt = 1
    
    for i in days[1:]:  # 첫 번째 제외하고 루프
        if current >= i:
            cnt += 1
        else:
            answer.append(cnt)
            current = i
            cnt = 1     # cnt 초기화
            
    answer.append(cnt)     # 마지막 묶음 append!! 중요
    return answer