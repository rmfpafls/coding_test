def solution(arr):
    two = 1
    flag = True
    
    while flag:
        if two >= len(arr): 
            flag = False
        else:
            two = two*2
        
    for i in range(two - len(arr)): 
        arr.append(0)
    return arr