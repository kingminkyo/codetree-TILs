n = int(input())

class User:
    def __init__(self, name, num, city):
        self.name = name
        self.num = num
        self.city = city

users = []

for _ in range(n):
    n, m, c = tuple(input().split())
    users.append(User(n,m, c))

low = users[0]

for u in users:
    if low.name < u.name:
        low = u

print(f"name {low.name}")
print(f"addr {low.num}")
print(f"city {low.city}")