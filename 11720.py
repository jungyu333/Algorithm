n = input()

numbers = list(input())



def solution(n , numbers):
    sum = 0

    for num in numbers:
        sum += int(num)

    return sum

print(solution(n,numbers))