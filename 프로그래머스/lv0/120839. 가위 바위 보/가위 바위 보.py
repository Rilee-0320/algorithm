def solution(rsp):
    answer = ''
    for x in rsp:
        if x == '2':
            answer += '0'
        elif x == '0':
            answer += '5'
        else:
            answer += '2'
    return answer