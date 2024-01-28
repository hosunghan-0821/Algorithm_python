# https://duwjdtn11.tistory.com/473 코드 참고
import sys

input = sys.stdin.readline
deque = list()


def push_front(num):
    global deque
    deque.insert(0, num)
    return


def push_back(num):
    global deque
    deque.append(num)
    return 0


def pop_front():
    global deque
    if len(deque) == 0:
        return -1
    else:

        return deque.pop(0)


def pop_back():
    global deque
    if len(deque) == 0:
        return -1
    else:
        return deque.pop(len(deque) - 1)


def size():
    global deque
    return len(deque)


def empty():
    global deque
    if len(deque) == 0:
        return 1
    else:
        return 0


def front():
    global deque
    if len(deque) == 0:
        return -1
    else:
        return deque[0]


def back():
    global deque
    if len(deque) == 0:
        return -1
    else:
        return deque[len(deque) - 1]


def solution():
    n = int(input())
    for i in range(n):
        command = input().strip()
        if "push_back" in command:
            command = command.split()
            push_back(int(command[1]))
        elif "push_front" in command:
            command = command.split()
            push_front(int(command[1]))
        elif command == "size":
            print(size())
        elif command == "front":
            print(front())

        elif command == "back":
            print(back())
        elif command == "empty":
            print(empty())
        elif command == "pop_front":
            print(pop_front())
        elif command == "pop_back":
            print(pop_back())
        else:
            print("error")


if __name__ == "__main__":
    solution()
