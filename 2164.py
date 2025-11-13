from collections import deque


def main():

    n = int(input())

    queue = deque()

    for i in range(n):
        queue.append(i + 1)


    while len(queue) > 1:
        queue.popleft()

        pop_item = queue.popleft()
        queue.append(pop_item)

    return queue[0]


if __name__ == '__main__':
    print(main())