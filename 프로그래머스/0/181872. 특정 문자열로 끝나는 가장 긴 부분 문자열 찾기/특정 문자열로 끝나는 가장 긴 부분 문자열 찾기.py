def solution(myString, pat):
    new_string = ""
    for i in range(len(myString) - len(pat), -1, -1):
        if myString[i:i+len(pat)] == pat:
            new_string = myString[:i+len(pat)] 
            break
    return new_string