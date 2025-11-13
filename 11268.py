from queue import PriorityQueue
import sys

def main():


    print = sys.stdout.write
    input = sys.stdin.readline
    n = int(input())
    myqueue = PriorityQueue()

    for i in range(n):
        request = int(input())
        if request == 0:
            if myqueue.empty():
                print('0\n')
            else:
                temp = myqueue.get()
                print(str((temp[1])) + '\n')
        else:
            myqueue.put((abs(request), i))

if __name__ == '__main__':
    main()