# 애초에 문제에서 yellow 개수가 brown 개수보다 많을 수 있는게 말이 됨?
def solution(brown, yellow):
    area = brown+yellow     #넓이
    # 그 다음에 약수 찾아야 되는데 흠.
    # 노랑 = (w-2) * (h-2) = wh -2w - 2h + 4
    # 갈색 = w*h - (w-2)*(h-2) = 2w + 2h + 4
    for w in range(area, 0, -1):    # 가로
        if area%w == 0:         # 나머지 없음
            h = area//w         # 세로 (약수)
            
            if (w >= h) and(2*w + 2*h - 4) == brown:
                return [w,h]