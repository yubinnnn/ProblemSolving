def solution(numbers):
    new_numbers = list(map(str, numbers))
    new_numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(int(''.join(new_numbers))))
