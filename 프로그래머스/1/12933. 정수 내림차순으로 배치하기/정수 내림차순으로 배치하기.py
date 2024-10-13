def solution(n):
    n = str(n)
    n_list = list(n)
    sorted_n = sorted(n_list)
    reverse_n = sorted_n[::-1]
    answer  = int(''.join(reverse_n))
    return answer
