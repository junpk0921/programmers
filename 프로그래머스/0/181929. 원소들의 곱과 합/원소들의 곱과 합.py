def solution(num_list):
    result1 = 1
    result2 = 0
    for i in num_list:
        result1 *= i
        result2 += i
    if result1 < result2**2:
        return 1
    else:
        return 0