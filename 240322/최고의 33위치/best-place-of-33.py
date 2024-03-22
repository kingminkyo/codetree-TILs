n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = 0

def count_area(x, y):
    count = 0
    for i in range(x, x+3):
        for j in range(y, y+3):
            if grid[i][j] == 1:
                count += 1

    return count



for i in range(n-2):
    for j in range(n-2):
        result = max(result, count_area(i, j))

print(result)