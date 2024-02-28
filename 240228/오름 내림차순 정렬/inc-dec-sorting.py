# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))

# 오름차순 정렬
arr.sort()

for elem in arr:
	print(elem, end=" ")
print()

# 내림차순 정렬
arr.sort(reverse=True)

for elem in arr:
	print(elem, end=" ")
print()