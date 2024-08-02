word = input()

final = []      
temp = word[0]

def comp():
    final = []      
    temp = word[0]
    cnt = 1
    for i in range(1, len(word)):
        
        if word[i] == word[i-1]:
            cnt += 1

            if i == (len(word)-1):
                final.append(word[i-1])
                final.append(cnt)

        else:
            final.append(word[i-1])
            final.append(cnt)
            temp = word[i]
            cnt = 1
            if i == (len(word)-1):
                final.append(word[i-1])
                final.append(cnt)
    # print(word)
    # print(final)
    return len(final)


import sys
result = sys.maxsize

for _ in range(len(word)):
    n = len(word)
    temp = word[n-1]
    word = list(word)

    for i in range(n-1, 0, -1):
        word[i] = word[i-1]
    word[0] = temp


    result = min(result, comp())

print (result)