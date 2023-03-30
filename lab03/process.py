'''
Author: Drew Meyer
KUID: 3020061
Date: 2/6/23
Lab: Lab 3
Last Accessed 2/6/23
Purpose: Process class which manages call stack.
'''

from stack import Stack
from function import Function

class Process:

   def __init__(self, name):
      self._name = name
      self._stack = Stack()

   def __str__(self):
      return f"{self._name}"

   def start(self):
      '''Represents start of new process.'''
      print(f"{self} started")

   def call(self, element):
      '''Represents function call within process stack.'''
      self._stack.push(element)
      print(f"{self} calls {element}")

   def my_return(self):
      '''Represents function return, process ends if main returns.'''
      if self._stack.is_empty():
         print(f"{self} process has ended.")
      else:
         my_return = self._stack.pop()
         print(f"{self} has {my_return} return")

   def my_raise(self):
      '''Represents exception raise, pop until exception handled.'''
      exception = self._stack.pop() # pop unhandled immediately
      print(f"{self} encountered a raised exception by: {exception}")
      print(f"{self} ends {exception} due to undandled exception")
      lcv = True # loop control variable
      while lcv:
         current_func = self._stack.peek() # check top of stack for node
         if current_func.entry._status == 'yes':
            print(f"{self} has exception handled by: {current_func.entry}")
            lcv = False
         else:
            unhandled = self._stack.pop()
            print(f"{self} ends {unhandled} due to unhandled exception")

