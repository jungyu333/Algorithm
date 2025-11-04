if __name__ == '__main__':

    import sys

    input = sys.stdin.readline

    N , M = map(int, input().split())
    numbers = list(map(int, input().split()))

    temp = 0
    sum = [0]

    for number in numbers:
        temp += number
        sum.append(temp)

    for i in range(M):
        s , e = map(int, input().split())

        print(sum[e] - sum[s - 1])
