'''
Author: Drew Meyer
KUID: 3020061
Date: 2/13/23
Lab: Lab 4
Last Accessed: 2/13/23
Purpose: Node class, represents object in linked list
'''

class Node:

   def __init__(self, entry):
      self.entry = entry
      self.next = None

   def __str__(self):
      '''Return human readable string.'''
      return f'{self.entry}'
