class Player:
    def __init__(self, userid, lv):
        self.userid = userid
        self.lv =  lv

    def ex_print(self):
        print(f"user {self.userid} lv {self.lv}")

a, b = input().split()

p1 = Player("codetree", 10)
p2 = Player(a, b)

p1.ex_print()
p2.ex_print()