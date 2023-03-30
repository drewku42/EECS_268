'''
Author: Drew Meyer
KUID: 3020061
Date: 2/6/23
Lab: Lab 3
Last Accessed: 2/6/23
Purpose: Class representing call stack architecture.
'''

from node import Node

class Stack:

   def __init__(self):
      self._top = None

   def push(self, entry):
      '''Adds to top of stack.'''
      new_node = Node(entry) # initialize new node
      new_node.next = self._top # assign new next node as top of stack
      self._top = new_node # assign new node to top of stack

   def is_empty(self):
      '''Returns True if stack is empty.'''
      if self._top == None: # if stack empty...
         return True
      else:
         return False

   def peek(self):
      '''Returns Node at top of stack.'''
      if not self.is_empty(): # if stack not empty
         return self._top # return top of stack
      else: # raise exception
         raise RuntimeError("Peek attempted on empty stack.")

   def pop(self):
      '''Remove top of stack.'''
      if not self.is_empty(): # if stack not empty
         current_top_value = self._top.entry # assign new node as top of stack
         self._top = self._top.next # assign next node as top
         return current_top_value # return node that was at top
      else: # raise exception
         raise RuntimeError("Pop attempted on empty stack.")

