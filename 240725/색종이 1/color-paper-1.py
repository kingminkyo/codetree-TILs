def calculate_blue_area(n, coordinates):
    # 100x100 격자판 생성
    grid = [[0] * 100 for _ in range(100)]
    
    # 각 색종이의 영역을 격자판에 표시
    for x, y in coordinates:
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                grid[i][j] = 1
    
    # 파란 영역의 넓이 계산
    blue_area = sum(sum(row) for row in grid)
    return blue_area

# 입력 받기
n = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(n)]

# 파란 영역의 넓이 계산 및 출력
result = calculate_blue_area(n, coordinates)
print(result)