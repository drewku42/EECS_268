'''
Author: Drew Meyer
KUID: 3020061
Date: 2/6/23
Lab: Lab 3
Last Accessed: 2/6/23
Purpose: Class representing call stack functions.
'''

class Function:

   def __init__(self, name, status):
      self._name = name
      self._status = status # exception handling, yes/no

   def __str__(self):
      return f"{self._name}"
