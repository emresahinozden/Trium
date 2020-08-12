#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 00:59:21 2020

@author: emre
"""

#%% Day 0: Hello, World

""" Task
To complete this challenge, you must save a line of input from stdin 
to a variable, print Hello, World. on a single line, 
and finally print the value of your variable on a second line."""

# Read a full line of input from stdin and save it to our 
# dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of 
# input_string to stdout.

print(input_string)

#%% Day 1: Data Types

"""
Task
Complete the code in the editor below. The variables i, d, and s are already 
declared and initialized for you. 

You must:
Declare 3 variables: one of type int, one of type double, and one of type String.
Read 3 lines of input from stdin (according to the sequence given in the 
Input Format section below) and initialize your  variables.
Use the  operator to perform the following operations:
Print the sum of i plus your int variable on a new line.
Print the sum of d plus your double variable to a scale of one decimal place on a new line.
Concatenate s with the string you read as input and print the result on a new line.
"""

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.
import sys
ii = int(sys.stdin.readline())
dd = float(sys.stdin.readline())
ss  = str(sys.stdin.readline())
# Print the sum of both integer variables on a new line.
print(i + ii)
# Print the sum of the double variables on a new line.
print(d + dd)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + ss)

#%% Day 2: Operators

"""
Task
Given the meal price (base cost of a meal), 
tip percent (the percentage of the meal price being added as tip), 
and tax percent (the percentage of the meal price being added as tax) for a meal, 
find and print the meal's total cost.
"""

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_total = tip_percent * meal_cost / 100
    tax_total = tax_percent * meal_cost / 100
    total_cost = round(meal_cost + tip_total + tax_total)
    print(total_cost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

#%% Day 3: Intro to Conditional Statements

"""
Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not n is weird.
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N % 2 == 1:
        print("Weird")
    elif N in range(2,6):
        print("Not Weird")
    elif N in range(6,21):
        print("Weird")
    else:
        print("Not Weird")
        
#%% Day 4: Class vs. Instance

"""
Write a Person class with an instance variable, age, 
and a constructor that takes an integer, initialAge, as a parameter. 
The constructor must assign initialAge to age after confirming the argument passed as  
initialAge is not negative; if a negative argument is passed as initialAge , 
the constructor should set age to 0 and print Age is not valid, 
setting age to 0.. In addition, you must write the following instance methods:

yearPasses() should increase the age instance variable by 1.
amIOld() should perform the following conditional actions:
If age < 13, print You are young..
If age >= 13 and <18, print You are a teenager..
Otherwise, print You are old..
To help you learn by example and complete this challenge, 
much of the code is provided for you, but you'll be writing everything in the future. 
The code that creates each instance of your Person class is in the main method. 
Don't worry if you don't understand it all quite yet!

Note: Do not remove or alter the stub code in the editor.
"""initialAge 

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge > 0:
            self.age = initialAge
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age = self.age + 1
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

#%% Day 5: Loops

"""
Given an integer, n, print its first 10 multiples. 
Each multiple n*i (where 1 <= i <= 10) should be printed on a new line 
in the form: n x i = result.
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

def ten_multiples(n):
    for i in range(1,11):
        print(str(n), "x", str(i), "=", str(n*(i)))

ten_multiples(n)

#%% Day 6: Let's Review

"""
Given a string, S, of length N that is indexed from 0 to N-1, 
print its even-indexed and odd-indexed characters as 2 space-separated strings 
on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.
"""

for i in range(int(input())):
    s = input()
    print(s[::2], s[1::2])
    
#%% Day 7: Arrays

"""
Given an array, A, of N integers, print A's elements in reverse order 
as a single line of space-separated numbers.
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in (arr[::-1]):
        print(i, end=" ")
        
#%% Day 8: Dictionaries and Maps

