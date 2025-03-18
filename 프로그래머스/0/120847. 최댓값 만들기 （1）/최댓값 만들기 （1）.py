def solution(numbers):
    answer = 0
    num = sorted(numbers, reverse=True)
    answer = num[0]*num[1]
    return answer