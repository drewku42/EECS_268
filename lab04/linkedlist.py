'''
Author: Drew Meyer
KUID: 3020061
Date: 2/13/23
Lab: Lab 4
Last Accessed 2/20/23
Purpose: Linked List Class
'''

from node import Node

class LinkedList:

   def __init__(self):
      self._front = None
      self._length = 0

   def length(self):
      '''Return length of list.'''
      return self._length

   def get_entry(self, index):
      '''Return entry at index.'''
      if self._length > 0:
         if 0 <= index < self._length: # if valid index
            jumper = self._front # initialize pointer variable
            for i in range(index):
               jumper = jumper.next
            return jumper # update and return pointer
         else:
            raise IndexError("Index out of range.")
      else:
         raise IndexError("List empty.")


   def insert(self, index, entry):
      '''Insert entry at index.'''
      if index == 0:
         my_entry = Node(entry) # initialize new entry
         my_entry.next = self._front # move front
         self._front = my_entry # set new entry to front of list
         self._length += 1 # incrament length

      elif 0 < index <= self._length:
         jumper = self.get_entry(index - 1) # obtain entry at desired index
         my_entry = Node(entry) # initialize new entry
         my_entry.next = jumper.next # set jumper next as entry next
         jumper.next = my_entry # set entry ahead of jupmer
         self._length += 1 # incrament length

      else:
         raise RuntimeError("Invalid index")

   def remove(self, index):
      '''Remove entry at index.'''
      if 0 <= index < self._length:
         if index == 0:
            self._front = self._front.next # set current front ahead one index
         else:
            jumper = self.get_entry(index - 1) # obtain desired index
            jumper.next = jumper.next.next # assign pointer two ahead of index

         self._length -= 1 # decrement length
      else:
         raise IndexError("Index out of range")


   def set_entry(self, index, entry):
      '''Sets an entry at a given index.'''
      if index < 0 or index >= self._length: # if nonvalid index...
         raise RuntimeError("Invalid index.")

      my_entry = Node(entry)
      current_entry = self.get_entry(index) # obtain entry
      current_entry._entry = my_entry # update entry

   def clear(self):
      '''Returns emptied list'''
      self._front = None
      self._length = 0
