
'''
Author: Drew Meyer
KUID: 3020061
Date: 2/13/23
Lab: Lab 4
Last Accessed: 2/21/23
Purpose: Class which imitates web browsing.
'''
from node import Node
from linkedlist import LinkedList

class WebBrowser():
   def __init__(self):
      self._list = LinkedList() # initialize linked list
      self._current = -1

   def navigate_to(self, url):
      '''Navigate to a url, removes each entry past the current url.'''
      if self._current == self._list.length() - 1:
         self._list.insert(self._list.length(), url)
         self._current += 1
      else:
         for index in range(self._list.length() - 1, self._current, -1):
            self._list.remove(index)
         self._list.insert(self._list.length(), url)
         self._current += 1


   def forward(self):
      '''If possible, moves current node forward one'''
      if self._current == self._list.length() - 1:
         self._current = self._current
      elif self._current < self._list.length() - 1:
         self._current += 1
      else:
         raise IndexError("Index out of range.")

   def back(self):
      '''If possible, moves current node back one.'''
      if self._current == 0:
         self._current = self._current
      elif self._current > 0:
         self._current -= 1
      else:
         raise IndexError("Index out of range.")


   def history(self):
      '''Prints formatted browser history.'''
      if self._list.length() == 0:
         print("No history available.\n")
      else:
         print("Oldest")
         print("-"*20)
         for index in range(self._list.length()): # for each entry in list
            if index == self._current:
               print(f"{self._list.get_entry(index).entry} <== current")
            else:
               print(f"{self._list.get_entry(index).entry}")
         print("-"*20)
         print("Newest\n")

