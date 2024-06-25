n = int(input())

class Student:
    def __init__(self, h, w, n):
        self.h, self.w = h, w
        self.n = n

students = []

for i in range(1, n+1):
    h, w = tuple(map(int, input().split()))
    students.append(Student(h, w, i))

students.sort(key= lambda x:(-x.h, -x.w, x.n))

for s in students:
    print(f"{s.h} {s.w} {s.n}")