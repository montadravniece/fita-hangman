with open('data/words.txt', 'r', encoding='utf-8') as file:
  words_all = file.read()

words_split = []
words_split = words_all.split("\n")

easy_words = []
medium_words = []
hard_words = []




with open('easy_words.txt', 'w', encoding='utf-8') as file:
  file.write(easy_words)

with open('medium_words.txt', 'w', encoding='utf-8') as file:
  file.write(medium_words)

with open('hard_words.txt', 'w', encoding='utf-8') as file:
   file.write(hard_words)