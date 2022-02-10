"""
# 4.
Write a program that takes in two words as input and returns a list containing three elements, in the following order Shared letters between two words.
Letters unique to word 1.
Letters unique to word 2.
Each element of the output should have unique letters, and should be alphabetically sorted. Useset operations. 
The strings will always be in lowercase and will not contain any punctuation.

Example:
Input1 sharp 
Input2 soap
Output ['aps', 'hr', 'o']

1. ortak, 
2. sadece birincide bulunanlar, 
3. sadece ikincide bulunanlar

"""

ltr_1 = input("Please type the first word: ")
ltr_2 = input("Please type the second word: ")

ltr_1 = ltr_1.lower() # string converted to lowercase
ltr_2 = ltr_2.lower() 

ltr_1 = set(ltr_1) # stirng converted to set 
ltr_2 = set(ltr_2)

inters = list(ltr_1.intersection(ltr_2)) # intersections and converting to the list
differs_1 = list(ltr_1.difference(ltr_2)) # differences 1  and converting to the list
differs_2 = list(ltr_2.difference(ltr_1)) # differences 2 and converting to the list

inters.sort() # sort ascending
differs_1.sort()
differs_2.sort()
    
inters_s = "" # empty string for converting list items
differs_1_s = ""
differs_2_s = ""

for i in inters: # slicing list items to save in empty string variable
    inters_s += str(i)
    
for j in differs_1:
    differs_1_s += str(j)

for k in differs_2:
    differs_2_s += str(k)

print(f"'{inters_s}', '{differs_1_s}', '{differs_2_s}'")