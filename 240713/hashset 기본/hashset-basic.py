n = int(input())
s = set()
for _ in range(n):
    command, x = tuple(input().split())
    x = int(x)

    if command == "add":
        s.add(x)
    elif command == "remove":
        s.remove(x)
    else:
        if x in s:
            print("true")
        else:
            print("false")