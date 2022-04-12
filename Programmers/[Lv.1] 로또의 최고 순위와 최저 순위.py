import random

def solution(lottos, win_nums):
    lottos = list(map(str,lottos))
    win_nums = list(map(str,win_nums))
    no = []
    new_lottos = []
    max_check = 0
    min_check = 0

    for i in win_nums:
        if i not in lottos:
            no.append(i)

    for num in lottos:
        if num == "0":
            no1 = random.choice(no)
            new_lottos.append(no1)
            no.remove(no1) 
        else:
            new_lottos.append(num)

    for i in new_lottos:
        if i in win_nums:
            max_check += 1

    for i in lottos:
        if i in win_nums:
            min_check += 1

    if max_check == 6:
        max_result = 1
    elif max_check == 5:
        max_result = 2
    elif max_check == 4:
        max_result = 3
    elif max_check == 3:
        max_result = 4
    elif max_check == 2:
        max_result = 5
    else:
        max_result = 6

    if min_check == 6:
        min_result = 1
    elif min_check == 5:
        min_result = 2
    elif min_check == 4:
        min_result = 3
    elif min_check == 3:
        min_result = 4
    elif min_check == 2:
        min_result = 5
    else:
        min_result = 6
    
    return [max_result, min_result]
