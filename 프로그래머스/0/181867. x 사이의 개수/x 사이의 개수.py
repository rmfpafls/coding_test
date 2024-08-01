def solution(myString):
    new_list = myString.split('x')
    print(new_list)
    count_list = []
    for i in range(len(new_list)):
        count_list.append(len(new_list[i]))
    return count_list