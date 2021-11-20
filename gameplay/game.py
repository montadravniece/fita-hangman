class Game:
    def __init__(self, word):
        self.word = word.upper()
        self.word_by_letters = list(self.word)
        self.length_of_word = len(self.word)
        
        self.lives = 6
        self.word_is_guessed = False
        
        self.empty_word = list(len(self.word) * "-")
        self.guessed_letters = list()
        self.missed_letters = list()
        self.missed_words = list()
       
    def draw(self):
        if self.lives == 6:
            print(
                "           \n",
                "           \n",
                "           \n",
                "           \n",
                "           \n",
                "___________\n"
            )
        elif self.lives == 5:
            print(
                "    _      \n",
                "   |       \n",
                "   |       \n",
                "   |       \n",
                "   |       \n",
                "___________\n"
            )
        elif self.lives == 4:
            print(
                "   ______  \n",
                "   |       \n",
                "   |       \n",
                "   |       \n",
                "   |       \n",
                "___________\n"
            )
        elif self.lives == 3:
            print(
                "   ______  \n",
                "   |    0  \n",
                "   |       \n",
                "   |       \n",
                "   |       \n",
                "___________\n"
            )
        elif self.lives == 2:
            print(
                "   ______  \n",
                "   |    0  \n",
                "   |    █  \n",
                "   |    █  \n",
                "   |       \n",
                "___________\n"
            )
        elif self.lives == 1:
            print(
                "   ______  ",
                "   |    0  ",
                "   |   /█\ ",
                "   |    █  ",
                "   |       ",
                "___________\n"
            )
        elif self.lives == 0:
            print(
                "   ______  ",
                "   |    0  ",
                "   |   /█\ ",
                "   |    █  ",
                "   |   / \ ",
                "___________\n"
            )
        
    def play (self):
        user_name = input("Hello! Please, enter your name: ")
        print("Hello, ", user_name, '\n',  'Word: ', self.empty_word, '\n', 'Word lenght = ', self.length_of_word, "\n", 'Your lives', self.lives)  

        while self.lives != 0 and self.word_is_guessed == False:
            print('\n')
            guess = input('Please type your letter: ').upper()
            length_of_guess = len(guess)
            # check lenght and if guess is aplhabetic
            if length_of_guess == 1 and guess.isalpha():
                if guess in self.guessed_letters: # Checking if letter is already guessed    
                    print("You have already tried this letter")

                if guess in self.word_by_letters:
                    # dzīvības nemainas
                    self.guessed_letters.append(guess) # Add guessed letter to guessed letters list
                    ########################################
                    for i, j in enumerate(self.word_by_letters): 
                        if j == guess:
                            self.empty_word[i] = guess # 'Open' correctly guessed letter    
                    #########################################
                    self.draw()
                    print(' Correct!', self.empty_word, '\n', 'Guess: ', self.guessed_letters, '\n', 'Missed: ', self.missed_letters, '\n', 'Missed words: ', self.missed_words, '\n', 'Lives: ', self.lives, '\n', 'Word lenght = ', self.length_of_word)
                    if self.empty_word == self.word_by_letters: # Check if word is guessed
                        self.word_is_guessed = True
                        break 
                else:
                    # dzīvības mīnusā
                    if guess in self.missed_letters:
                        print("You have already tried this letter")
                    else:
                        self.lives = self.lives - 1
                        self.missed_letters.append(guess)
                        self.draw()
                        print(' Wrong!', self.empty_word, '\n', 'Guess: ', self.guessed_letters, '\n', 'Missed: ', self.missed_letters, '\n', 'Missed words: ', self.missed_words, '\n', 'Lives: ', self.lives, '\n', 'Word lenght = ', self.length_of_word)
            else:
                if guess in self.missed_words:
                        print("You have already tried this word")
                elif length_of_guess == self.length_of_word and guess.isalpha():
                    if guess == self.word:
                        self.word_is_guessed = True
                        self.empty_word = self.word
                        break
                    else:
                        self.missed_words.append(guess)
                        self.lives = self.lives - 1
                        print(' Wrong!', self.empty_word, '\n', 'Guess: ', self.guessed_letters, '\n', 'Missed: ', self.missed_letters, '\n', 'Missed words: ', self.missed_words, '\n', 'Lives: ', self.lives, '\n', 'Word lenght = ', self.length_of_word)
                else:
                    if length_of_guess > self.length_of_word and guess.isalpha():
                        print("Sorry, ", user_name, "the word you entered is too long!")
                        print(self.empty_word, '\n', 'Guess: ', self.guessed_letters, '\n', 'Missed: ', self.missed_letters, '\n', 'Missed words: ', self.missed_words, '\n', 'Lives: ', self.lives, '\n', 'Word lenght = ', self.length_of_word)
                    elif length_of_guess < self.length_of_word and guess.isalpha():
                        print("Sorry, ", user_name, "the word you entered is too short!")
                        print(self.empty_word, '\n', 'Guess: ', self.guessed_letters, '\n', 'Missed: ', self.missed_letters, '\n', 'Missed words: ', self.missed_words, '\n', 'Lives: ', self.lives, '\n', 'Word lenght = ', self.length_of_word)
                    else:
                        print("Wrong input type!")
                        print('\n', 'Guess: ', self.guessed_letters, '\n', 'Missed: ', self.missed_letters, '\n', 'Missed words: ', self.missed_words, '\n', 'Lives: ', self.lives, '\n', 'Word lenght = ', self.length_of_word)
        if self.word_is_guessed == True:
            print("Congratulations! You won! The correct word was:", self.word, "!")
        elif self.lives == 0:
            print("Sorry! Game over! Correct word was", self.word, '!')
        else:
            print("What just happend?")


            
            
        