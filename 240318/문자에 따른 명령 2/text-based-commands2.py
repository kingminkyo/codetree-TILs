lr = input()


dir_num = 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0





for i in range(len(lr)):

    if lr[i] == "L":
        # print("hello")
        dir_num -= 1

    elif lr[i] == "R":
        dir_num += 1 
    else :
        x, y = x+dx[dir_num], y+dy[dir_num]

    # print(f"{x} {y}")
    dir_num = (dir_num  ) % 4

print(f"{x} {y}")