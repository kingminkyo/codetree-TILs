n = int(input())
arr = list(map(int, input().split()))

words = []
for a in arr:
    words.append(a)
    mid = int(len(words)/2) -1
    words.sort()

    if a % 2 == 1:
        # print(words)
        print(words[mid], end=" ")