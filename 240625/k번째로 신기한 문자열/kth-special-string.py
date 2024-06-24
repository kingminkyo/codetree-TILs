n, k, t = tuple(input().split())
n, k = int(n), int(k)

words = []
sz = len(t)

for _ in range(n):
    w = input()
    if w[:sz] == t:
        words.append(w)

words.sort()

print(words[k-1])