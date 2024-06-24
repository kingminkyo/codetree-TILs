n, k, t = tuple(input().split())
n, k = int(n), int(k)

words = []

for _ in range(n):
    w = input()
    if w[:2] == t:
        words.append(w)

words.sort()

print(words[k-1])