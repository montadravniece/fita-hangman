from gameplay.game import Game
import random

words = 'seja', 'zakis', 'ziepes'


while True:

    game = Game(random.choice(words))
    game.play()
    
    exit_ = str(input('do you want to exit? y/n: '))
    if exit_ == 'y':
        break
    else:
        continue
