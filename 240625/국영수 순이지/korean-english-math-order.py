class Person:
    def __init__(self, name, kor, eng, math):
        self.name, self.kor, self.eng, self.math = name, kor, eng, math


n = int(input())
persons = []

for _ in range(n):
    n, k, e, m = tuple(input().split())
    k, e, m = int(k), int(e), int(m)
    persons.append(Person(n, k, e, m))

persons.sort(key = lambda x: (-x.kor, -x.eng, -x.math))

for p in persons:
    print(f"{p.name} {p.kor} {p.eng} {p.math}")