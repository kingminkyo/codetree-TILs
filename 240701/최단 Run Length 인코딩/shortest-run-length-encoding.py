word = input()

def incoding(word):

    new_word = []
    cnt = 1
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            cnt += 1 
        else:
            new_word.append(word[i-1])
            new_word.append(cnt)
            cnt = 1
        
        if i == (len(word)-1):
            new_word.append(word[i-1])
            new_word.append(cnt)

    if new_word[1] == 10:
        return 3

    return len(new_word)


min_result = 10000
word = list(word)

for _ in range(len(word)):
    temp = word[len(word)-1]

    for i in range(len(word)-1, 0, -1):
        word[i] = word[i-1]
    word[0] = temp

    min_result = min(incoding(word), min_result)

print(min_result)