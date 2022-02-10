"""
# 2.
Write a program that takes two inputs; 
one of them is a list and the other is a number, 
and returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative). 
Use wrap-around if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list.

Example:

Inputs [1, 2, 3, 4, 5], 2
Output [4, 5, 1, 2, 3] 
Inputs [1, 2, 3, 4, 5], -2 
Output [3, 4, 5, 1, 2]

"""
import collections # 

x = int(input("Please type a number for the list: "))
lst = list(range(1, x+1))

n = int(input("Please type the number for shifting amout: "))

a_lst = collections.deque(lst)

a_lst.rotate(n)

shifted_lst = list(a_lst)

print(shifted_lst)