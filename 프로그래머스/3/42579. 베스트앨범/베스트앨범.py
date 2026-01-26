# 제일 많이 들은 장르 찾기
# 장르 내에서 많이 들은 노래 찾기
# 반복 ?
def solution(genres, plays):
    answer = []
    count = {}      # 장르별 카운트
    songs = {}      # 장르 속 곡별 카운트
    
    for i in range(len(genres)):
        if genres[i] not in count:
            count[genres[i]] = plays[i]
        else:
            count[genres[i]] += plays[i]
        if genres[i] not in songs:
            songs[genres[i]] = []       # key값 저장 및 value는 빈 리스트
        songs[genres[i]].append((i, plays[i]))    # 인덱스와 재생횟수
            
    sorted_genres = sorted(count.keys(), key=lambda g: count[g], reverse=True)

    for genre in sorted_genres:
        song = sorted(songs[genre], key=lambda x: (-x[1], x[0]))
        for i, (idx, _) in enumerate(song):
            if i >= 2:
                break
            answer.append(idx)
    return answer