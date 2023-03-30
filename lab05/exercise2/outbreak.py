'''
Author: Drew Meyer
KUID: 3020061
Date: 2/22/23
Lab: Lab 5
Last Accessed: 2/22/23
Purpose: Calculates the total number of sick people.
'''

def outbreak(day):
   '''Returns number of sick on given day.'''
   if day <= 0:
      return None
   elif day == 1:
      return 6
   elif day == 2:
      return 20
   elif day == 3:
      return 75
   else: # dayN sick: dayN-3 + dayN-2 + dayN-1
      return outbreak(day-3) + outbreak(day-2) + outbreak(day-1)

def main():
   print("OUTBREAK!")
   dayN = int(input("What day do you want a sick count for?: "))
   if dayN <= 0:
      print("Invalid day")
   else:
      print(f"Total people with flu: {outbreak(dayN)}")

main()
