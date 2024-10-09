def solution(n):
    flag = 1
    x = 1
    while flag:
        if n % x == 1: 
            flag = 0
        else: 
            x += 1
    return x