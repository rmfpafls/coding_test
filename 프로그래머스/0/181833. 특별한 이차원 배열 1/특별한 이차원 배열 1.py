def solution(n):
    answer = []
    for i in range(n):
        element = [1 if j == i else 0 for j in range(n)]
        answer.append(element)
    return answer