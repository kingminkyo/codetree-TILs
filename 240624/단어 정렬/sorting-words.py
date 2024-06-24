n = int(input())

words = []
for _ in range(n):
    words.append(input())

words.sort()

for w in words:
    print(w)