import random

user_name = str(input("Hello user. Please, enter your name!"))
print("Hello, ", user_name ,"\U0001f600"),

# game variables

words= 'LIETUS', "ANDROID", "VASARA"
word = random.choice(words)
length_of_word = len(word)
word_by_letters = list(word)
empty_word = list(length_of_word * "-")

lives = 6
word_is_guessed = False
guessed_letters = list()
guessed_word_set = set(word)
missed_letters = list()
missed_words = list()

# game code
while True:
    while lives != 0 and word_is_guessed == False:
        guess = input('Please type your letter: ').upper()
        length_of_guess = len(guess)
        # check lenght and if guess is aplhabetic
        if length_of_guess == 1 and guess.isalpha():
            if guess in guessed_letters: # Checking if letter is already guessed    
                print("You have already tried this letter")

            if guess in word_by_letters:
                # dzīvības nemainas
                guessed_letters.append(guess) # Add guessed letter to guessed letters list
                ########################################
                for i, j in enumerate(word_by_letters): 
                    if j == guess:
                        empty_word[i] = guess # 'Open' correctly guessed letter    
                #########################################
                print('Correct!', empty_word, '\n', 'Guess: ', guessed_letters, '\n', 'Missed: ', missed_letters, '\n', 'Missed words: ', missed_words, '\n', 'Lives: ', lives)
                if empty_word == word_by_letters: # Check if word is guessed
                    word_is_guessed = True
                    break 
            else:
                # dzīvības mīnusā
                if guess in missed_letters:
                    print("You have already tried this letter")
                else:
                    lives = lives - 1
                    missed_letters.append(guess)
                    print('Wrong!', empty_word, '\n', 'Guess: ', guessed_letters, '\n', 'Missed: ', missed_letters, '\n', 'Missed words: ', missed_words, '\n', 'Lives: ', lives)
        else:
            if guess in missed_words:
                    print("You have already tried this word")
            elif length_of_guess == length_of_word and guess.isalpha():
                if guess == word:
                    word_is_guessed = True
                    empty_word = word
                    break
                else:
                    missed_words.append(guess)
                    lives = lives - 1
                    print('Wrong!', empty_word, '\n', 'Guess: ', guessed_letters, '\n', 'Missed: ', missed_letters, '\n', 'Missed words: ', missed_words, '\n', 'Lives: ', lives)
            else:
                if length_of_guess > length_of_word and guess.isalpha():
                    print("Sorry, ", user_name, "the word you entered is too long!")
                    print(empty_word, '\n', 'Guess: ', guessed_letters, '\n', 'Missed: ', missed_letters, '\n', 'Missed words: ', missed_words, '\n', 'Lives: ', lives)
                elif length_of_guess < length_of_word and guess.isalpha():
                    print("Sorry, ", user_name, "the word you entered is too short!")
                    print(empty_word, '\n', 'Guess: ', guessed_letters, '\n', 'Missed: ', missed_letters, '\n', 'Missed words: ', missed_words, '\n', 'Lives: ', lives)
                else:
                    print("Wrong input type!")
                    print(empty_word, '\n', 'Guess: ', guessed_letters, '\n', 'Missed: ', missed_letters, '\n', 'Missed words: ', missed_words, '\n', 'Lives: ', lives)
    if word_is_guessed == True:
        print("Congratulations! You won! The correct word was:", word, "!")
    elif lives == 0:
        print("Sorry! Game over! Correct word was", word, '!')
    else:
        print("What just happend?")


    exit_ = str(input('do you want to exit? y/n'))
    if exit_ == 'y':
      break
    else:
        continue