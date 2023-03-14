from .die import Die
from .die import roll

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def reroll_dice(self): # BUGFIX 2: Created this function to isolate rerolling of dice, as the init also resets the score! Rewrote it to use the die.roll function
        roll(self.dice)

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value # BUGFIX 1: Fixed this to add the value of the die, instead of just 1
        return total

    @classmethod
    def run(cls):
        # c: Counts consecutive wins.
        c = 0
        runner = cls() # BUGFIX 2: Moved instantiation to outside game loop, to avoid resetting rounds, wins, losses
        while True:
            runner.reroll_dice() # BUGFIX 2: Reroll dice here instead of instantiating, to avoid resetting 

            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you guessed correctly!")
                runner.wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                #print("Like seriously, how could you mess that up")
                runner.loses += 1
                c = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if c == 6:
                print("You won! Well done! Congrats!")
                #print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[(y)/n]: ") 

            if prompt != 'n' and prompt != 'N':  # FIX 3: Default is to continue now, you have to abort with n or N
                continue
            else: # FIX 3: Erased this exception throwing for a proper exit message
                print('Okay, quiting the game.') 
                print('You played {} rounds, and the final score was: '.format(runner.round))
                print('Wins: {}, Losses: {} '.format(runner.wins, runner.loses))
                print('You were on a streak of {} consecutive wins.'.format(c))
                break
