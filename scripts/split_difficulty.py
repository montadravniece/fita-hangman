with open('data/words.txt', 'r', encoding='utf-8') as file: 
  words_all = file.read()

words_split = []
words_split = words_all.split("\n")

easy_words = []
medium_words = []
hard_words = []

hard_letters = ['Ā', 'Č', 'Ē', 'Ģ', 'Ī', 'Ķ', 'Ļ', 'Ņ', 'Š', 'Ū', 'Ž']

#### cikls, kas izveido jaunu sarakstu ar vārdiem, kuros ir 'grūtie' burti
# for words in words_split:
#     for character in hard_letters:
#         if character in words:
#             hard_words.append(words)
####


######## izveido vārdnīcu -> katram vārdam unikālo simbolu skaits
unique_count_word = {}
for word in words_split:
  unique_count_word[word] = len(set(word))

print(unique_count_word)
########


#### cikls, kas vienkārši sadala visus vārdus 3 sarežģītības pakāpēs tikai pēc vārda garuma
for word in words_split:
  if len(word) < 4:
    easy_words.append(word)
  elif len(word) > 14:
    hard_words.append(word)
  else:
    medium_words.append(word)
####

print(easy_words)


with open('data/easy_words.txt', 'w', encoding='utf-8') as file: 
  file.write(easy_words)

with open('data/medium_words.txt', 'w', encoding='utf-8') as file:
  file.write(medium_words)

with open('data/hard_words.txt', 'w', encoding='utf-8') as file:
  file.write(hard_words)
