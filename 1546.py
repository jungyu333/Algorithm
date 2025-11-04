


def solution(N, scores):
    answer = 0

    # 최대 점수
    M = max(scores)

    # 전체 점수 합
    sum = 0

    for score in scores:
        sum += score

    answer = sum * 100 / M / int(N)

    return answer


if __name__ == '__main__':
    N = input()

    scores = list(map(int, input().split()))

    result = solution(N, scores)

    print(result)