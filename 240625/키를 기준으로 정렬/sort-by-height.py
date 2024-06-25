n = int(input())

class Person:
    def __init__(self, name, tall, weight):
        self.name , self.tall, self. weitht = name, tall, weight

persons = []
for _ in range(n):
    n, t, w = tuple(input().split())
    t, w = int(t), int(w)

    persons.append(Person(n, t, w))

persons.sort(key = lambda x:x.tall)

for p in persons:
    print(f"{p.name} {p.tall} {p.weight}")