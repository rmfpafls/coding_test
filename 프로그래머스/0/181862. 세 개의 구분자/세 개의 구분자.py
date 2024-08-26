def solution(myStr):
    for char in 'abc':
        myStr = myStr.replace(char, '|')
    
    answer = myStr.split('|')
    
    answer = [item for item in answer if item]
    
    if answer == []: 
        answer = ["EMPTY"]
    return answer