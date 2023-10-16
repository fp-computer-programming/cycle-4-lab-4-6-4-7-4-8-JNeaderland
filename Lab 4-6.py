"""

*** You must write a comment for every chunk of code you write from now on along with your author tag***
4-6
Create a Python file named lab_4-6.py
Write a program that asks for user input for an animal and a dish. 
Your program should print true or false to indicate whether the beast is allowed to bring the dish to the feast 
(the first letter of the animal is the same as the first and last letter of the dish).
Assume that beast and dish are always lowercase strings, and that each has at least two letters. 
beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string. They will not contain numbers.

"""
#Author: Jacob Neaderland
animal = input ("What animal are you? ")
dish = input ("What dish would you like? ")
if animal[0] == dish [0]:
    print ("true")
else:
    print ("false")