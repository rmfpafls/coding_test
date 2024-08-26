def solution(binomial):
    lst = binomial.split()
    if lst[1] == "+":
        return int(lst[0]) +int(lst[-1])
    elif lst[1] == "-":
        return int(lst[0]) -int(lst[-1])
    else:
        return int(lst[0]) * int(lst[-1])
