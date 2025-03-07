def solution(str):
    new = ''
    for i in str:
        if i.isupper():
            new += i.lower()
        else : 
            new += i.upper()
    return new