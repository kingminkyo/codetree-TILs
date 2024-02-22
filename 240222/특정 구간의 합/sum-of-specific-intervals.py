# n, m = tuple(map(int, input().split()))
# A = list(map(int,input().split()))
# a[][] = list
# for i in range(m):
#     a[m] = list(map(int,input().split()))


n, m = tuple(map(int, input().split()))
A = list(map(int, input().split()))
a = []  # 이중 리스트 초기화
for i in range(m):
    a.append(list(map(int, input().split())))  # 각 입력을 리스트로 변환하여 추가


for i in range(m):
    result = 0
    for j in range(a[i][0], a[i][1]+1):
        # print(j)
        result += A[j-1]

    print(result)