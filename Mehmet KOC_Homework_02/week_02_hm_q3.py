"""
# 3.
Write a code snippet that inputs a sentence from the user, then uses a dictionary to summarize the number of occurrences of each letter. 
Ignore case, ignore blanks and assume the user does not enter any punctuation. 
Display a two-column table of the letters and their counts with the letters in sorted order. Example:

Input  This is a sample text with several words This is more sample text with some different words 

Output[('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1), ('o', 4), 
('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]

"""
sentence = input("Please type a sentence for counting the letters: ")

count = {} # empty dictionary to save the letter from given sentence

for i in sentence: # to take every letter from the sentence and lower it. Then if the letter is in the dictionary (named count) increase it's value
    if i in count:
        count[i.lower()] = count[i.lower()] + 1
    elif i == " ": #if the letter is blank do not write in the count dictionay
        pass
    else:
        count[i.lower()] = 1 # if the letter is not in the dictionary write it as a key and assign 1 as a value

sorted_count = sorted(count.items()) # sorted dictionary as ascending

print(sorted_count)