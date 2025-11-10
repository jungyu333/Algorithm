
def main():

    answer = 0

    import sys
    input = sys.stdin.readline

    N = int(input())

    numbers = list(map(int, input().split()))

    numbers.sort()

    for k in numbers:
        start, end = 0, N - 1

        while start < end:

            i , j = numbers[start], numbers[end]

            if i + j == k:

                if i != k and j != k:
                    answer += 1
                    break
                elif i == k:
                    end += 1
                else:
                    start += 1

            elif i + j > k:
                end -= 1

            else:
                start += 1


    return answer


if __name__ == '__main__':
    print(main())