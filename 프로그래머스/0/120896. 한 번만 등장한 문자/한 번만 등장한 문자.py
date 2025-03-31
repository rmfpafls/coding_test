def solution(s):
    count = {}  # 문자 개수를 저장할 딕셔너리
    
    # 문자 개수 세기
    for i in s: 
        if i in count:  # 키가 존재하는지 확인
            count[i] += 1
        else:
            count[i] = 1  # 키가 없으면 초기화
            
    # 한 번만 등장한 문자 필터링 후 정렬
    answer = ''.join(sorted([char for char in count if count[char] == 1]))       
    return answer