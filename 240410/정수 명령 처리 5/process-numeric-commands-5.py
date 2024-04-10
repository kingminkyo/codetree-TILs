arr = []
n = int(input())


for _ in range(n):
    command = input()
    if command.startswith("push_back"):
        a, num = tuple(command.split())
        arr.append(int(num))

    elif command.startswith("pop"):
        arr.pop()

    elif command.startswith("size"):
        print(len(arr))

    else:
        a, index = tuple(command.split())
        print(arr[int(index)-1])