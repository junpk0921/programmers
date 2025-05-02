def solution(num_list):
    add = 0
    odd = 1
    if len(num_list) >= 11:
        for i in num_list:
            add += i
        return add
    else:
        for i in num_list:
            odd *= i
        return odd