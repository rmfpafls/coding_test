def solution(arr, n): 
    count_arr = len(arr)
    if count_arr % 2 == 0: # 짝수라면
        for i in range(1,count_arr, 2):  
            arr[i] = arr[i] + n
    else: 
        for i in range(0, count_arr,2): 
            arr[i] = arr[i] +n
    return arr