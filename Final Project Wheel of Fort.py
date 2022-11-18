# #! PART A

class WOFPlayer:
    prizeMoney = 0
    prizes = []
    def __init__(self, name) -> None:
        self.name = name
    
    def addMoney(self, amt):
        return self.prizeMoney + amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
        return self.prizeMoney
    
    def addPrize(self, prize):
        return self.prizes.append(prize)    
    
    def __str__(self) -> str:
        return f"{self.name} {(self.prizeMoney)}"
    
# #! PART B