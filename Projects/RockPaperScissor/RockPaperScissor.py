import random
class RPS:
    
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.computer_score = 0
        self.player_score = 0
        self.rounds = 5
    
    def random_choice(self):
        return random.choice(self.choices)
    
    def get_input(self):
        while True:
            user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print("Invalid input. Please enter rock, paper, or scissors.")

    def start_game(self):
        for i in range(self.rounds):
            user_choice = self.get_input()
            computer_choice = self.random_choice()
            print(f"\nComputer chose {computer_choice}.\n")

            if user_choice == computer_choice:
                print(f"Both players selected {user_choice}. It's a tie!")
            elif user_choice == 'rock':
                if computer_choice == 'scissors':
                    print('Rock smashes scissors! You win this round')
                    self.player_score += 1
                else:
                    print('Paper covers rock! You lose this round')
                    self.computer_score += 1
            elif user_choice == 'paper':
                    if computer_choice == 'rock':
                        print('Paper covers rock! You win this round')
                        self.player_score += 1
                    else:
                        print('Scissors cuts paper! You lose this round')
                        self.computer_score += 1
            elif user_choice == 'scissors':
                        if computer_choice == 'paper':
                            print('Scissors cuts paper! You win this round')
                            self.player_score += 1
                        else:
                            print('Rock smashes scissors! You lose this round')
                            self.computer_score += 1
        print(f"Score - You: {self.player_score}, Computer: {self.computer_score}")

rps = RPS()
rps.start_game()
    
