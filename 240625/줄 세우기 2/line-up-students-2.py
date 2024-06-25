class Student:
    def __init__(self, h, w, n):
        self.h = h
        self.w = w
        self.n = n

n = int(input())

students = []
for i in range(1,1+n):
    h, w = map(int, input().split())
    students.append(Student(h, w, i))

students.sort(key= lambda x:(x.h, -x.w))

for s in students:
    print(f"{s.h} {s.w} {s.n}")