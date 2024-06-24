n = int(input())

class Date:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

dates = []


for _ in range(n):
    dt, dy, wt = tuple(input().split())
    dates.append(Date(dt, dy, wt))

fast = Date("9999-99-99", "", "")

for d in dates:
    if d.weather == "Rain" and (fast.date > d.date):
        fast = d

print(f"{fast.date} {fast.day} {fast.weather}")