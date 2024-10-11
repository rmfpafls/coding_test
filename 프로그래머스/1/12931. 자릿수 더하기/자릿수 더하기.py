def solution(n):
    answer = 0
    n_str = str(n)
    n_list = list(n_str)
    for i in range(len(n_list)): 
        answer += int(n_list[i])
    return answer