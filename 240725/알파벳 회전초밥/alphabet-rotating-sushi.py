dust = input()
word = input()

cnt = 0

cycle = 0 

while cnt != len(word):

    cycle += 1

    for c in dust:
        if c == word[cnt]:
            cnt += 1
        if cnt == len(word):
            break
    # print(cnt, cycle)
    
print(cycle)