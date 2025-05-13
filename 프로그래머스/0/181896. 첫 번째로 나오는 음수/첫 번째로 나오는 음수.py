def solution(num_list):
    result = -1
    for idx, val in enumerate(num_list):
        if val < 0:
            result = idx
            break
    return result