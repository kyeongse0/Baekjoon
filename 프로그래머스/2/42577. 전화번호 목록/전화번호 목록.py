# 집합을 써야 하는 구나...가 왜 바로 안떠오를까?
# 가 아니라 여러 번 어떻게? 비교하지?
def solution(phone_book):
    phone_num = set(phone_book)
    for phone in phone_num:
        for i in range(1, len(phone)):
            prefix = phone[:i]
            if prefix in phone_num:
                return False
            else:
                pass
    return True