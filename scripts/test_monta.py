with open('data/words.txt', 'r', encoding='utf-8') as file:
    file_contents = file.read()
    all_words = file_contents.split("\n")
    # print(all_words)
    # list = ["easy", "medium", "hard"]
    # print("\nlist items: ")
    # print (list [0])
    # print (list [1])
    # print (list [2])
    easy_words = []
    medium_words = [] 
    hard_words = []
    
    for word in all_words:
        if len(word) < 7:
            easy_words.append(word)
        elif len(word) > 12:
            hard_words.append(word)
        else:
            medium_words.append(word)
    print(len(easy_words))
    print(len(medium_words))
    print(len(hard_words))
    
    