n = int(input())
d = dict()
ans = 0
for _ in range(n):
    word = input()

    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

    ans = max(ans, d[word])

print(ans)