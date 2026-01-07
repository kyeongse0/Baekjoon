def solution(s):
    opened = []

    for i in s:
        if i == '(':
            opened.append('(')
        elif i == ')':
            if len(opened) == 0:
                return False
            opened.pop()
    return len(opened) == 0