def main():
    N = int(input())

    numbers = [i for i in range(1, N + 1)]
    start_index = 0
    end_index = 0
    total_sum = 1
    answer = 0

    while start_index < N:
        if total_sum == N:
            answer += 1

        if total_sum >= N:
            total_sum -= numbers[start_index]
            start_index += 1
        else:
            end_index += 1
            if end_index == N:
                break
            total_sum += numbers[end_index]

    return answer


if __name__ == '__main__':
    print(main())
