'''
Author: Drew Meyer
KUID: 3020061
Date: 4/2/23
Lab: Lab 7
Last Accessed: 4/2/23
Purpose: Class representing pokemon with id, us name, jp name.
'''

class Pokemon:

   def __init__(self, us_name=None, number=None, jp_name=None):
      self._us_name = us_name
      self._number = int(number)
      self._jp_name = jp_name

   def __str__(self):
      '''Returns human readable string representing a given pokemon.'''
      return f"Pokemon({self._us_name}, {self._number}, {self._jp_name})"

   def __lt__(self, other):
      '''Returns True if pokemon number less than another.'''
      if self._number < other._number:
         return True
      else:
         return False

   def __gt__(self, other):
      '''Returns True if pokemon number greater than another.'''
      if self._number > other._number:
         return True
      else:
         return False

   def __eq__(self, other):
      '''Returns True if pokemon numbers are the same.'''
      if self._number == other._number:
         return True
      else:
         return False
