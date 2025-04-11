def solution(num_list):
    odd = ""
    even = ""
    result = ""

    for i in num_list:
        if i%2 == 1:
            odd += str(i)
        else:
            even += str(i)
    result = int(odd)+int(even)
    return result
        