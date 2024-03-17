arr = [list(map(int, input().split())) for _ in range(19)]
# print(arr)

start = 0
win = 0
win_color = 0
x1 = 0
x2 = 0

for i in range(19):
    for j in range(19):
        start = 0

        if arr[i][j] is not 0:
            # print("hello")
            start = arr[i][j] 
            win = 0

            for k in range(1, 5):
                if arr[i][j+k] == start:
                    win += 1
            if win is not 4:
                win = 0
            if win == 0:
                for k in range(1, 5):
                    if arr[i+k][j+k] == start:
                        win += 2
                if win is not 8:
                    win = 0
            if win == 0:
                for k in range(1, 5):
                    if arr[i+k][j] == start:
                        win += 3
                if win is not 12:
                    win = 0
                
            if win >= 1:
                win_color = start
                if win == 4:
                    x1, x2 = i+1, j+3 
                elif win == 8:
                    x1, x2 = i+3, j+3
                else :
                    x1, x2 = i+3, j+1 
                break
            
        if win >= 1:
            break
    if win >= 1:
            break

print(win_color)
print(f"{x1} {x2}")