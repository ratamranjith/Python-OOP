import random


class NumberGuess:
    def __init__(self):
        self.number = None
        self.guessCount = 0
        self.generatedNumber = 0

    def generate_random(self):
        self.generatedNumber = random.randint(1, 1000)

    def give_clue(self):
        if self.number == 0:
            print("Guess a number between 1 and 1000")
        else:
            if self.generatedNumber > self.number:
                print("Too low, try again")
                self.guessCount += 1
            elif self.generatedNumber < self.number:
                print("Too high, try again")
                self.guessCount += 1
            else:
                print("You guessed it in {self.guessCount} attempts")


num = NumberGuess()
num.generate_random()
while num.guessCount <= 5:
    num.number = int(input("Guess a number between 1 and 1000"))
    print(num.give_clue())
else:
    print(f"generated number is : {num.generatedNumber}")
