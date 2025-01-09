def solution(arr, k):
    lst = []
    for num in arr:
        if num not in lst:  # 중복 제거
            lst.append(num)
            if len(lst) == k:  # 원하는 길이에 도달하면 종료
                break
    
    # 리스트가 k보다 짧으면 나머지를 -1로 채우기
    while len(lst) < k:
        lst.append(-1)
    
    return lst
