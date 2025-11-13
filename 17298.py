def main():

    n = int(input())

    numbers = list(map(int, input().split()))

    stack = []

    answer = [0 for i in range(n)]

    for i in range(n):

        while stack and (numbers[stack[-1]] < numbers[i]):
            answer[stack.pop()] = numbers[i]

        stack.append(i)


    while len(stack) > 0:
        index = stack.pop()
        answer[index] = -1

    return answer

if __name__ == '__main__':
    print(main())
