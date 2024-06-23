class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

Players = []

for _ in range(5):
    n, s = input().split()
    s = int(s)

    Players.append(Player(n, s))

low = Players[0]

for p in Players:
    if low.score > p.score:
        low = p


print(f"{low.name} {low.score}")