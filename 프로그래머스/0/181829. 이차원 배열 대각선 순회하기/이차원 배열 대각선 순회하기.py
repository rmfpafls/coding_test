def solution(board, k):
    cnt = 0
    len_board = len(board)
    for i in range(len_board): 
        for j in range(len(board[i])):
            if i+j < k or i+j == k:
                cnt += board[i][j]     
    return cnt 