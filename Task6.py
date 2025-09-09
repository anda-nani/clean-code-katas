def longest(words_list: str) :

    longest_word = max(words_list, key=len) #find longest word by length

    for word in words_list:
        if len(word) == len(longest_word): #compare the length of the longest word with the list
            print(f"{word}") 

longest(["the", "quick", "brown", "fox", "ate", "my", "chickens"])

longest(["once", "upon", "a", "time"])