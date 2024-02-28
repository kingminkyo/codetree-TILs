n = int(input())
word_list = [
    input()
    for i in range(n)
]

word_list.sort()

for w in word_list:
    print(w)