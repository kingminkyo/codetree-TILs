word = input()

count = dict()

for w in word:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

key = True
for k, v in count.items():
    if v == 1:
        print(k)
        key = False
        break

if key:
    print("None")