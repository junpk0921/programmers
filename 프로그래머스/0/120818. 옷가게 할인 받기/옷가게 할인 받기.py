import math

def solution(price):
    if price>=100000 and price<300000:
        return math.floor(price*0.95)
    elif price>=300000 and price<500000:
        return math.floor(price*0.9)
    elif price>=500000:
        return math.floor(price*0.8)
    else:
        return math.floor(price)
