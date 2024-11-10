def solution(seoul):
    for idx, elm in enumerate(seoul): 
        if elm == "Kim": 
            return f"김서방은 {idx}에 있다"