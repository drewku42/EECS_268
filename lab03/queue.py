'''
Author: Drew Meyer
KUID: 3020061
Date: 2/6/23
Lab: Lab 3
Last Accessed: 2/6/23
Purpose: Queue data structure representation.
'''

from node import Node

class Queue:

   def __init__(self):
      self._front = None
      self._back = None

   def is_empty(self):
      '''If queue empty, return True.'''
      if self._front == None:
         return True

   def enqueue(self, entry):
      '''Add new node to front of queue.'''
      my_node = Node(entry)
      if self.is_empty(): # if there are no nodes in current queue
         self._front = my_node # assign node to front and back
         self._back = my_node
      else: # if there is at least one node in queue
         self._back.next = my_node # set new node as next to back node
         self._back = my_node # set new node as new back of queue
      print(f"{entry} added to queue. ")

   def dequeue(self):
      '''Remove node from queue.'''
      if self.is_empty():
         raise RuntimeError("Dequeue attempted on empty queue.")
      elif self._front is self._back:
         self._front = None
         self._back = None
      else: # if queue has more than one node...
         self._front = self._front.next

   def peek_front(self):
      '''Return front of queue.'''
      return self._front.entry
