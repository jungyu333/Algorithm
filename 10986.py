def main():
    answer = 0

    import sys



    input = sys.stdin.readline

    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))

    partial_sum = [0] * N

    partial_sum[0] = numbers[0]

    remained = [0] * M

    # 부분합
    for i in range(1, N):
        partial_sum[i] = partial_sum[i - 1] + numbers[i]

    for i in range(N):
        remain = partial_sum[i] % M
        remained[remain] += 1
        if remain == 0:
            answer += 1

    for i in range(M):

        if remained[i] > 0:
            answer += (remained[i] * (remained[i] - 1) // 2)


    return answer







if __name__ == '__main__':
    result = main()

    print(result)