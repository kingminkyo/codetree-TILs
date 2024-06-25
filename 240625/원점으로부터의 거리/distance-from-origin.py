n = int(input())

class Dist:
    def __init__(self, x, y, n):
        self.x, self.y, self.n = x, y, n
        self.man = abs(x) + abs(y)

dists = []

for i in range(1, n+1):
    x, y = map(int, input().split())
    dists.append(Dist(x, y, i))

dists.sort(key = lambda x:x.man)

for d in dists:
    print(f"{d.n}")