
with open('../hangman/data/words.txt', 'r', encoding='utf-8') as file:  ##jānorāda pilnais ceļš!
    words_all = file.read()


words_split = words_all.split("\n")

def get_number_of_elements(words_split):
    count = 0
    for element in words_split:
        count += 1
    return count
a = get_number_of_elements(words_split)

for number in range(a):
    print(number)


# words_dict = dict.fromkeys(number)
# print(words_dict)

d = {number:words_split}
print(d)

easy_words = []
medium_words = []
hard_words = []

hard_letters = ['Ā', 'Č', 'Ē', 'Ģ', 'Ī', 'Ķ', 'Ļ', 'Ņ', 'Š', 'Ū', 'Ž']

# indices = [i for i, x in enumerate(words_split) if x == hard_letters]
# print(indices)

# if hard_letters in words_split:
#     var = [i for i, d in enumerate(words_split) if d == hard_letters]
#
#     for index, e in enumerate(words_split):
#         d[e].append(index)

# print(words_split.pop())
# a = list()
# for index, word in enumerate(words_split):
#     print(index, word)
# a = [e for hard_letters, e in enumerate(a) if hard_letters not in words_split]
# print(a)


# print(easy_words)
