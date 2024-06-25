class Person:
    def __init__(self, n, h, w):
        self.n, self.h, self.w = n, h, w

# n = int(input())
persons = []
for _ in range(5):
    n, h, w = tuple(input().split())
    h, w = int(h), float(w)

    persons.append(Person(n, h, w))

print("name")
persons.sort(key = lambda x:x.n)

for p in persons:
    print(f"{p.n} {p.h} {p.w}")
print()

print("height")
persons.sort(key = lambda x: -x.h)

for p in persons:
    print(f"{p.n} {p.h} {p.w}")