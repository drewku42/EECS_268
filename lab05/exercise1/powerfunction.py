'''
Author: Drew Meyer
KUID: 3020061
Date: 2/22/23
Lab: Lab 5
Last Accessed: 2/22/23
Purpose: Function which takes a base and raises to a power.
'''

def powerfunction(base, power):
   '''Raises base to power.'''
   if power < 0:
      return None
   elif power == 0:
      return 1
   else:
      return base * powerfunction(base, power - 1)


def main():
   running = True
   while running:
      num1 = int(input("Enter a base: "))
      num2 = int(input("Enter a power: "))
      if num2 < 0:
         print("Exponent must be zero or greater. ")
      else:
         print(f"Answer: {powerfunction(num1, num2)}")
         running = False

main()
