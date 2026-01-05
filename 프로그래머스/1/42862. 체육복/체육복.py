# 1. 여벌 체육복을 가졌으면서 도난당한 학생 여부 확인
# 2. 해당 학생 reserve에서 제외
# 3. 여기서 집합을 생각했어야 함...

def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    
    # 여벌을 가지고 있는 객체를 돌면서 해야지!!!1
    for student in sorted(reserve_set):
        if student - 1 in lost_set:
            lost_set.remove(student-1)
        elif student + 1 in lost_set:
            lost_set.remove(student+1)
            
    answer = n - len(lost_set)
    return answer