from collections import Counter
def solution(participant, completion):
    test = list((Counter(participant)-Counter(completion)).elements())
    return test.pop()
