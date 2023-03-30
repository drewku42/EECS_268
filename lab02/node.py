'''
Author: Drew Meyer
KUID: 3020061
Date: 1/30/23
Lab: Lab 2
Last Accessed: 1/30/23
Purpose: Node class, represents object within stack.
'''

class Node:

   def __init__(self, entry):
      self.entry = entry
      self.next = None # object 'on top' of the current object

