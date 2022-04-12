from itertools import permutations

def solution(numbers):
    answer = []
    nums = list(numbers)
    per = []
    for i in range(1, len(numbers)+1):
        per += list(permutations(nums, i)) # i개씩 순열조합
    new_nums = [int(("").join(p)) for p in per] # 각 순열조합을 하나의 int형 숫자로
    
    for n in new_nums:
        if n < 2: # 2보다 작은 1,0의 경우 소수 아님
            continue
        check = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                check = False
                break
        if check:
            answer.append(n)
            
    return len(set(answer))
