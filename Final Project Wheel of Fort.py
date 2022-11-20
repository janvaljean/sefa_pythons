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


class WOFHumanPlayer(WOFPlayer):
    
    def getMove(self, category, obscuredPhrase, guessed):
        print(f"{self.name} has ${self.prizeMoney}\n\nCategory: {category}\nPhrase: {obscuredPhrase}\nGuessed: {guessed}\n\nGuess a letter,phrase or type 'exit' or 'pass':")
        guessed = input().upper
        if guessed == 'exit':
            return "exit the game"
        elif guessed == 'pass':
            return "skip your turn"
        
# ! PART C


class WOFComputerPlayer(WOFPlayer):
    import random
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    super().__init__()
    self.difficulty = 2

    def smartCoinFlip(self):
        if self.difficulty < random.randint(1, 10):
            return False
        else:
            return True

    def getPossibleLetters(self, guessed):
        LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        LETTERS.pop(guessed)
        VOWELS = list('AEIOU')
        VOWEL_COST = 250
        if self.prizeMoney < VOWEL_COST:
            for v in VOWELS:
                LETTERS.pop(v)
        return LETTERS

    def getMove(self, category, obscuredPhrase, guessed):
        getPossibleLetters(guessed)
        if LETTERS == VOWELS and self.prizeMoney < VOWEL_COST:
            return 'pass'

        elif smartCoinFlip(self) == True:
            return SORTED_FREQUENCIES[-1]
        elif smartCoinFlip(self) == False:
            random.choice(getPossibleLetters())
