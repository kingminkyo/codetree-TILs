n = int(input())
arr = list(map(int, input().split()))

words = []
for i in range(len(arr)):
    words.append(arr[i])
    mid = int(len(words)/2) 
    words.sort()
    
    if (i+1) % 2 == 1:
        print(words[mid], end=" ")
        # print(words)