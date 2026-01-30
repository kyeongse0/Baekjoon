import heapq
from collections import Counter

def solution(operations):
    # 최소힙
    min_heap = []
    # 최대힙 (음수로 저장)
    max_heap = []
    # ✅ 추가: 실제 남아있는 값들의 개수 추적
    count = Counter()
    
    for operation in operations:
        if "I" in operation:
            num = int(operation[2:])
            # 최대 최소 힙에 둘다 푸쉬
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            count[num] += 1  # ✅ 카운트 증가
            
        elif operation == "D 1" and max_heap:
            # 최대값 제거
            # ✅ 이미 삭제된 값(count==0)은 건너뛰기
            while max_heap and count[-max_heap[0]] == 0:
                heapq.heappop(max_heap)
            
            if max_heap:
                max_val = -heapq.heappop(max_heap)
                count[max_val] -= 1  # ✅ 카운트 감소
                
        elif operation == "D -1" and min_heap:
            # 최소값 제거
            # ✅ 이미 삭제된 값(count==0)은 건너뛰기
            while min_heap and count[min_heap[0]] == 0:
                heapq.heappop(min_heap)
            
            if min_heap:
                min_val = heapq.heappop(min_heap)
                count[min_val] -= 1  # ✅ 카운트 감소
    
    # ✅ 마지막 정리: 삭제된 값들 제거
    while min_heap and count[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and count[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    
    # ✅ 안전한 반환
    if not min_heap or not max_heap:
        return [0, 0]
    
    return [-max_heap[0], min_heap[0]]
