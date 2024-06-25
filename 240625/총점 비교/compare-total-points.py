class Student:
    def __init__(self, n, a, b, c):
        self.n, self.a, self.b, self.c = n, a, b, c
        self.total = a+b+c

n = int(input())

students = []
for _ in range(n):
    n, a, b, c = tuple(input().split())
    a, b, c = int(a), int(b), int(c)
    students.append(Student(n, a, b, c))

students.sort(key = lambda x:-x.total)

for s in students:
    print(f"{s.n} {s.a} {s.b} {s.c}")