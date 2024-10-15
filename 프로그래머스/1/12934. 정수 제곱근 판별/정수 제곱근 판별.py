def solution(n):
    result = n ** 0.5
    if result.is_integer():
        return (result+1)**2
    else:
        return -1