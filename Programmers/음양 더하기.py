def solution(absolutes, signs):
    signs = list(signs)
    for i in range(len(absolutes)):
        if signs[i] == True :
            absolutes[i] = absolutes[i] * 1
        else:
            absolutes[i] = absolutes[i] * (-1)
    return sum(absolutes)
