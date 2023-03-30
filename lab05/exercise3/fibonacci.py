'''
Author: Drew Meyer
KUID: 3020061
Date: 2/22/23
Lab: Lab 5
Last Accessed: 2/22/23
Purpose: Produce or verify a given Fibonacci number.
'''

def fib(num):
   '''Returns the nth Fibonacci number.'''
   if num <= 1:
      return num
   else:
      return fib(num - 1) + fib(num - 2)

def is_fib(num):
   '''Returns true if num in fib sequence'''
   if num < 0:
      return False # invalid input
   elif num == 0 or num == 1: # base cases
      return True
   else:
      count = 1 # variable to incrament each loop
      while fib(count) <= num: # while fib of count less than num
         if fib(count) == num: # if fib of count is num
            return True # num is in sequence
         count += 1
      return False # num not in sequence


def main():
   '''Runs user interaction.'''
   print("Good Old Fibonacci")
   print("Modes: '-i' for ith term, '-v' for verify term. \n" + "-"*50)
   user_input = input("Enter '-i' or '-v' followed by integer. ")

   mylist = user_input.split(' ')
   if mylist[0] == '-i':
      mynum1 = int(mylist[1])
      mynum2 = fib(mynum1)
      print(f"Term {str(mynum1)} is {str(mynum2)}. ")

   elif mylist[0] == '-v':
      mynum = mylist[1]
      if is_fib(int(mynum)):
         print(f"{mynum} is in the sequence. ")
      else:
         print(f"{mynum} is not in the sequence. ")

   else:
      print("Invalid input. ")

main()
