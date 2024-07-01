word = input()





def incoding(word):

    new_word = []
    cnt = 0
    for i in range(1, len(word)-1):
        if word[i] == word[i-1]:
            cnt += 1 
        else:
            new_word.append(word[i-1])
            new_word.append(chr(cnt))

    return len(new_word)

print(incoding(word))