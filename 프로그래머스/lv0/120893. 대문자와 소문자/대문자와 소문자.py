def solution(my_string):
    answer = ''
    for str in my_string:
        if str.islower() == True:
            answer += str.upper()
        else:
            answer += str.lower()
    return answer