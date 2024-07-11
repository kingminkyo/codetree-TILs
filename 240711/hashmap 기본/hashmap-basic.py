n = int(input())
d = dict()

for _ in range(n):
    command = input()

    if command.startswith("add"):
        _, a, b = tuple(command.split())
        a, b = int(a), int(b)
        d[a] = b
    elif command.startswith("find"):
        _, a = tuple(command.split())
        a = int(a)
        if a not in d:
            print("None")
        else:            
            print(d[a])
    else:
        _, a = tuple(command.split())
        a = int(a)
        d.pop(a)