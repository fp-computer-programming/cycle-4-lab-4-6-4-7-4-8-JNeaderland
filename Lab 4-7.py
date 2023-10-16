
""""

4-7
Create a Python file named lab_4-7.py
Write a program that prompts a uses 5 inputs to prompt a user for a number. 
Store all numbers as a single string with a space in between each numbers 
(i.e num_string = ‘1 2 3 4 5’). Print this string. Using string methods, 
extract the smallest and largest number from the string & print them, 
with a label (i.e smallest num given was 1). 
Print the product of the two numbers you have extracted, with a label (i.e. the product of the two numbers extracted was 5).

"""
num1 = int (input ("What is your first number? "))
num2 = int (input ("What is your second number? "))
num3 = int (input ("What is your third number? "))
num4 = int (input ("What is your fourth number? "))
num5 = int (input ("What is your fifth number? "))
num_string = "{0}, {1}, {2}, {3}, {4}".format(num1, num2, num3, num4, num5)
print (num_string)

num_list = [num1, num2, num3, num4, num5]
num_list.sort()
lownum = num_list[0]
highnum = num_list[4]
multnum = lownum * highnum
print ("the lowest number given was " + str(lownum))
print ("the highest number given was " + str(highnum))
print ("The product of the highest and lowest numbers was " + str(multnum))


