# 소요 시간, 요청 시각, 작업 번호 작은 순
# 작업 반환 시간의 평균

import heapq

def solution(jobs):
    # 현재 시각
    time = 0
    # 총 걸린 시간(요청~완료까지의 합)
    total = 0
    # 몇 개 처리했는지
    done = 0
    # 최소 힙 (소요 시간, 요청 시각, 작업 번호)
    heap = []
    # 요청 시각 순으로 정렬
    jobs = sorted(enumerate(jobs), key=lambda it: it[1][0])
    
    idx = 0  # 아직 힙에 안 넣은 jobs의 인덱스
    n = len(jobs)
    
    while done < n: # 요청을 다할때까지
        while idx < n and jobs[idx][1][0] <= time:
            job_idx, (start, length) = jobs[idx]
            heapq.heappush(heap, (length, start, job_idx))
            idx += 1
        if heap:    # 만약 대기중인게 있다면 가장 소요시간이 짧은 걸 꺼내기
            length, start, job_idx = heapq.heappop(heap)
            # 현재 시각을 이 작업 끝나는 시점으로 이동
            time += length
            # 이 작업의 요청~완료까지 걸린 시간 더하기
            total += time - start
            done += 1
        else:
            # 대기 중인 작업이 없으면, 시간을 다음 작업 요청 시각으로 점프 !!!
            time = jobs[idx][1][0]
    return total // n