# """"
# Please write a program which prints out all the even numbers between two and thirty, 
# using a loop. Print each number on a separate line.
# The beginning of your output should look like this:
# """
# num = 14

# while True:
    
#     if num >= 2:
#         if num < 30:
#             if num % 2 == 0:
#                 print(num)
#         else:
#             break            
             
    
#     num += 1
# print("etc...")    
                   

# # Fix the program
# print("Are you ready?")
# number = int(input("Please type in a number: "))
# while number != 0:
#     print(number)
#     number -= 1
# print("Now!")


# """

# Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.

# Sample output
# Upper limit: 5
# 1
# 2
# 3
# 4

# Please don't use the value True as the condition of your while loop in this exercise!

# """
# up_lim = int(input("Upper limit: ")) 
# num = 1

# while num < up_lim:
#         print(num)
#         num = num + 1

# upper_lim = int(input("Upper limit: "))
# base = int(input("Base: "))
# num = 1


# while num < (upper_lim + 1):
#         print(f"{num}")
#         num = num * base

# limit = int(input("Limit: "))
# sum = 0
# num = 0

# while sum < limit:
#         num = num + 1
#         sum += num
        
# print(sum)    
    

"""
Please write a new version of the program in the previous exercise. 
In addition to the result it should also print out the calculation performed:

Sample output
Limit: 2
The consecutive sum: 1 + 2 = 3

Sample output
Limit: 10
The consecutive sum: 1 + 2 + 3 + 4 = 10

Sample output
Limit: 18
The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

You may assume the number typed in by the user is always equal to 2 or higher.

"""

# limit = int(input("Limit: "))
# sum = 0
# num = 0
# con_sum = "The consecutive sum: "

# while sum < limit:
#         num = num + 1
#         sum += num
#         if num == 1:
#                 con_sum += f" {num}"
#         else:    
#                 con_sum += f" + {num}"     

# print(f"{con_sum} = {sum}")
  


"""
Please write a program which asks the user for a string and an amount. The program then prints out the string as many times as specified by the amount. The printout should all be on one line, with no extra spaces or symbols added.

An example of expected behaviour:

Sample output
Please type in a string: hiya
Please type in an amount: 4
hiyahiyahiyahiya

"""
# str_1 = input("Please type in a string: ")
# mul_1 = int(input("Please type in an amount: "))

# print(f"{str_1 * mul_1}")

""""
Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

Some examples of expected behaviour:

Sample output
Please type in string 1: hey
Please type in string 2: hiya
hiya is longer

Sample output
Please type in string 1: howdy doody
Please type in string 2: hola
howdy doody is longer

Sample output
Please type in string 1: hey
Please type in string 2: bye
The strings are equally long

"""
# str_1 = input("Please type in string 1: ")
# str_2 = input("Please type in string 2: ")

# if len(str_1) > len(str_2):
#     print(f"{str_1} is longer")
# elif len(str_1) < len(str_2):
#     print(f"{str_2} is longer")
# else:
#     print(f"The strings are equally long")



"""

Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

An example of expected behaviour:

Sample output
Please type in a string: hiya
a
y
i
h

"""
# str_101 = input("Please type in a string: ")
# index = -1

# while index < len(str_101):
#     print(str_101[index])
#     index -= 1


# str_1 = input("Please type in a string: ")
# index = -1

# while abs(index) <= len(str_1) :
#     print(str_1[index])
#     index -= 1

""""
Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.

Sample output
Please type in a string: python
The second and the second to last characters are different

Sample output
Please type in a string: pascal
The second and the second to last characters are a
"""

# word = input("Please type in a string: ")

# if len(word) > 1 and word[1] == word[-2]:
#     print(f"The second and the second to last characters are {word[1]}")
# else:
#      print("The second and the second to last characters are different")


"""
Please write a program which prints out a line of hash characters, 
the width of which is chosen by the user.
"""

# width = int(input("Width: "))
# height = int(input("Height: "))
# symbl = "#"

# while height > 0:
#     print(f"{width * symbl}")
#     height -= 1


# while True:
#     str_1 = input("Please type in a string: ")

#     if len(str_1) == 0:
#         break
#     else:
#         print(str_1)
#         print("-" * len(str_1))


"""
Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Sample output
Please type in a string: python

**************python
Sample output
Please type in a string: alongerstring

*******alongerstring
Sample output
Please type in a string: averyverylongstring

*averyverylongstring
"""

# str_1 = input("Please type in a string: ")
# req_length = 20

# if len(str_1) < req_length:
#     print("*" * (req_length - len(str_1)) + str_1)
# else:
#     print(str_1)    
    

# word = input("Word: ")
# total_width = (30 - 2) # 1-1 space left for stars
# len_word = len(word)

# total_padding = total_width - len_word

# left_padding = total_padding // 2
# right_padding = total_padding - left_padding

# str_mid = "*"+" " * left_padding + word + " " * right_padding + "*"
# print("*" * 30)
# print(str_mid)
# print("*" * 30)


"""
Please write a program which asks the user to type in a string. 

The program then prints out all the substrings which begin with the first character, 

from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
te
tes
test
"""

# word = "test"

# print(word[-1:])
# print(word[-2:])
# print(word[-3:])
# print(word[-4:])

# word = input("Please type in a string: ")
# len_word = len(word)
# index = -1

# while abs(index) < (len_word + 1) :
#     print(word[index:])
#     index -= 1

"""
Please write a program which asks the user to input a string. 
The program then prints out different messages.
if the string contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. 
Have a look at the examples below.

Sample output
Please type in a string: hello there
a not found
e found
o found

Sample output
Please type in a string: hiya
a found
e not found
o not found
"""

# str_vo = input("Please type in a string: ").lower()
# vowels = "aeo"
# index = 0

# while index < len(vowels):
#     vowel = vowels[index]

#     if vowel in str_vo:
#         print(f"{vowel} found")
#     else:
#         print(f"{vowel} not found")    
#     index += 1


# word = input("Please type in a word: ")
# char = input("Please type in a character: ")
# output = ""

# while True:
#     index_char = word.find(char)
    
#     # Break the loop if the character is not found
#     if index_char == -1:
#         break
    
#     # Check if there are enough characters for a substring of length 3
#     if index_char < len(word) - 2:
#         output = word[index_char:index_char+3]
#         print(output)
    
#     # Update the word to exclude the current processed character
#     word = word[index_char + 1:]



# str = "abababa"
# sub_str = "aba"

# first_index = str.find(sub_str)

# if first_index == -1:
#     print("The substring does not occur twice in the string.")
# else:
#     second_index = str.find(sub_str, first_index + len((sub_str)))

#     if second_index == -1:
#         print("The substring does not occur twice in the string.")
#     else:
#         print(f"The second occurrence of the substring is at index {second_index}.")


"""
Please write a program which asks the user for a positive integer number. 
The program then prints out a list of multiplication operations until both operands reach the number given by the user. 
See the examples below for details:
"""

# num_user = int(input("Please type in a number:"))

# for i in range(1, num_user + 1):
#     for j in range(1, num_user + 1):
#         result  = i * j
#         print(f"{i} x {j} = {result}")

# print("new")    
# for j in range(1, num_user + 1):
#     for i in range(1, num_user + 1):
#         result  = i * j
#         print(f"{i} x {j} = {result}") 

        
"""
Please write a program which asks the user to type in a sentence. 
The program then prints out the first letter of each word in the sentence,
 each letter on a separate line.
 
 """

# sentence_1 = input("Please type in a sentence:")

# results = ""
# previous_char = " "
        
# for char in sentence_1:
#     if char != " " and previous_char == " ":
#         results += char
#         print(char)
#     previous_char = char

"""
Please write a program which asks the user to type in an integer number. 
If the user types in a number equal to or below 0, the execution ends. 
Otherwise the program prints out the factorial of the number.

The factorial of a number involves multiplying the number by all the positive integers smaller than itself. In other words, it is the product of all positive integers less than or equal to the number. 
For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.
"""


# while True:
#     num = int(input("Please type in a number: "))

#     if num <= 0:
#         print("Thanks and bye!")
#         break

#     fact = 1
#     for i in range(1, num+1):
#         fact = fact * i

#     print(f"The factorial of the number {num} is {fact}")    

"""
Please write a program which asks the user to type in a number. 
The program then prints out all the positive integer values from 1 up to the number. 
However, the order of the numbers is changed so that each pair or numbers is flipped. 
That is, 2 comes before 1, 4 before 3 and so forth.
See the examples below for details.
"""

# num = int(input("Please type in a number: "))

# i = 1

# while i <= num:
#     if i + 1 <= num:
#         print(i+1)
#         print(i)
#         i += 2 

#     else:
#         print(i)
#         i += 1


"""
Please write a program which asks the user to type in a number. 
The program then prints out the positive integers between 1 and the number itself, 
alternating between the two ends of the range as in the examples below.

"""

num = int(input("Please type in a number: "))

start = 1
end = num

while start <= end:
    print(start)
    start += 1

    if start <= end:
        print(end)
        end -= 1


