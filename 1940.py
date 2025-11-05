def main():

    import sys

    input = sys.stdin.readline

    N = int(input())
    M = int(input())

    numbers = list(map(int, input().split()))

    numbers.sort()

    start = 0
    end = N - 1

    answer = 0

    while start <= end:
        if numbers[start] + numbers[end] == M:
            answer += 1
            start += 1
            end -= 1

        elif numbers[start] + numbers[end] < M:
            start += 1

        else:
            end -= 1

    return answer


if __name__ == '__main__':
    print(main())