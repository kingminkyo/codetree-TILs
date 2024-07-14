n, m = tuple(map(int, input().split()))
A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

ans = 0
s = set()


def check(x, y, z):

    s.clear()


    for i in range(n):
        s.add(A[i][x] + A[i][y] + A[i][z])

    for i in range(n):
        if (B[i][x] + B[i][y] + B[i][z]) in s:
            return False
        
    return True

for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            if check(i, j, k): ans+= 1

print(ans)