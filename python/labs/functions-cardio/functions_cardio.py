# Exercise 1: longest_word
# Write a function longest_word that accepts three arguments, each representing a string. Return the longest word among the three strings.


def longest_word(w1, w2, w3):
 l1 = len(w1)
 l2 = len(w2)
 l3 = len(w3)
 if l1 > l2 and l1 > l3:
   return w1
 elif l2 > l1 and l2 > l3:
   return w2
 else:
   return w3

print(longest_word("a","aa","aaa"))
 
 
 
# Exercise 2: reverse_string
# Write a function reverse_string that accepts one argument as a string, and returns the string with its letters reversed. For example, "hello!" becomes "!olleh".
# Solution 1:
 
 
def reverse_string(string):
 rev_str=""
 for i in range(len(string)):
   rev_str = rev_str + string[len(string)-1-i]
 return rev_str
 
print(reverse_string("This string"))
 
 
# Solution 2:
 
 
def reverse_string(string):
 return string[::-1]
print(reverse_string("This string"))
 
 
 
# Exercise 3: sum_to_n
# Write a function sum_to_n that takes one argument as an integer num, and returns the sum of 1 + 2 + ... + num. Example: sum_to_n(4) returns 10 (1 + 2 + 3 + 4).
 
 
def sum_to_n(num):
 sum = 0
 for i in range(num):
   sum = sum + i + 1
 return sum
print(sum_to_n(5))
 
 
 
# Exercise 4: is_triangle
# Write a function is_triangle that takes three arguments, s1, s2, and s3, that represent the lengths of the three sides of a triangle. This is a valid triangle if the sum of two lengths is always greater than the third. Return True if the three arguments represent a valid triangle, or False if they do not.
 
 
def is_triangle(s1, s2, s3):
 if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
   return True
 else:
   return False
 
print(is_triangle(3,3,5))
 
 
 
# Exercise 5: roll_dice
# Write a function roll_dice that takes in an argument num representing the number of 6-sided dice to roll, and returns the sum of the n rolls. Simulate rolling that number of 6-sided die using import random and random.randint(1, 6) to generate a random number between 1 and 6 inclusive. Remember that if you are rolling for 2 dice, it's not as simple as running random.randint(2, 12)! You must roll each die individually to maintain realistic chances - rolling a 2 is much more rare than rolling a 7!
 
from random import randint
 
def roll_dice(num):
 sum = 0
 for i in range(num):
   roll = randint(1, 6)
   sum = sum + roll
 return sum
 
print(roll_dice(4))
 
 
 
# Extension #1: is_prime
# Write a function is_prime that takes in one integer as an argument and determines whether it is a prime number or not. As a reminder, a prime number is only divisible by 1 and itself. is_prime should return True or False depending on whether the number is prime.
 
 
def is_prime(num):
 for i in range(2, num):
   if(num % i == 0):
     return False
 return True
 
print(is_prime(7))
print(is_prime(8))
 
 
 
# Extension #2: snake_case
# Write a function snake_case that takes in a string in camelCase (like you would write variables in JavaScript), and converts it to snake_case, converting everything to lowercase and separating by underscores. You can assume that each capital letter is the start of a new word. Use string slicing to get "parts" of a word.
 
 
def snake_case(string):
 snake_string = ""
 for i in range(len(string)):
   if string[i] == string[i].upper():
     snake_string = snake_string + "_" + string[i].lower()
   else:
     snake_string = snake_string + string[i]
 return snake_string
 
print(snake_case("convertThisStringToSnakeCase"))
 
 
 
 
 
 
 
 







