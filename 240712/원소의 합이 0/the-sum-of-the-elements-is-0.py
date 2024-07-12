n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

count = dict()
ans = 0 

for i in range(n):
    for j in range(n):
        for k in range(n):
            for m in range(n):
                sum_val = A[i] + B[j] + C[k] + D[m]
                if sum_val == 0:
                    ans += 1 

print(ans)