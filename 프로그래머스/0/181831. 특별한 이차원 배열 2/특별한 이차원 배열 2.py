def solution(arr):
    len_arr = len(arr) 
    answer = 1
    for i in range(len_arr):
        for j in range(len_arr): 
            if arr[i][j] != arr[j][i]: 
                answer = 0
    return answer 
