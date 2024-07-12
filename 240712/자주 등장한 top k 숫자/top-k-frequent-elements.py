m, k = map(int, input().split())
arr = list(map(int, input().split()))

count = {}

# 각 요소의 빈도수를 계산
for a in arr:
    if a in count:
        count[a] += 1
    else:
        count[a] = 1

# Number 클래스를 정의하여 keys와 value를 저장
class Number:
    def __init__(self, keys, value):
        self.keys = keys
        self.value = value

# 빈도수 딕셔너리를 Number 객체의 리스트로 변환
numbers = [Number(key, value) for key, value in count.items()]

# 빈도수와 keys 기준으로 내림차순 정렬
numbers.sort(key=lambda x: (-x.value, -x.keys))

# 상위 k개의 keys를 출력, k가 numbers의 길이보다 크면 numbers의 길이까지만 출력
for i in range(min(k, len(numbers))):
    print(numbers[i].keys, end=" ")