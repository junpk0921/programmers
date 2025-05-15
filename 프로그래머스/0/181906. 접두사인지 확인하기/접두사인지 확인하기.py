def solution(my_string, is_prefix):
    for i in range(len(is_prefix)):
        if i >= len(my_string) or my_string[i] != is_prefix[i]:
            return 0
    return 1