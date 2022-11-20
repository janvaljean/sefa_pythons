import random
VOWEL_COST = 250
LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
VOWELS = 'AEIOU'
# #! PART A

class WOFPlayer():
    def __init__(self, name) -> None:
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    
    def addMoney(self, amt):
        return self.prizeMoney + amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
        return self.prizeMoney
    
    def addPrize(self, prize):
        return self.prizes.append(prize)    
    
    def __str__(self) -> str:
        return f"{self.name} ${self.prizeMoney}"
    
# #! PART B


class WOFHumanPlayer(WOFPlayer):

    def getMove(category, obscuredPhrase, guessed):
        str = input(self.name + "has $" + str(self.prizeMoney) + "/n" + ", Category:" + category + "/n" + ", Phrases:" +
                    "/n" + obscuredPhrase + "/n" + ", Guessed:" + guessed + "/n" + "Guess a letter, phrase, or type 'exit' or 'pass':")
        print(str)
        
# ! PART C


class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    prizemoney = 0
    def __init__(self):
        super().__init__()
        self.difficulty = difficulty

    def smartCoinFlip(self):
        if random.randint(1, 10) > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        lst = list(LETTERS)
        for c in guessed:
            lst.remove(c)       
        if self.prizeMoney < VOWEL_COST:
            for l in lst:
                lst.remove(l)
        return lst

    def getMove(self, category, obscuredPhrase, guessed):
        lst  
        if getPossibleLetters(self, guessed) == VOWELS and self.prizeMoney < VOWEL_COST:
            return 'pass'

        elif smartCoinFlip(self) == True:
            return SORTED_FREQUENCIES[-1]
        elif smartCoinFlip(self) == False:
            return random.choice(getPossibleLetters())
