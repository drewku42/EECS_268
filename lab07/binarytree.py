'''
Author: Drew Meyer
KUID: 3020061
Date: 3/27/23
Lab: Lab 7
Last Accessed: 3/27/23
Purpose: Binary tree data structure.
'''

from node import BinaryNode as bn
from pokemon import Pokemon

class BinaryTree:

   def __init__(self):
      self._root = None

   def _add_rec(self, entry, cur_node):
      '''Navigates through binary tree until an empty leaf is found.'''
      if entry < cur_node._entry:
         if cur_node._left is None:
            cur_node._left = bn(entry)
         else:
            self._add_rec(entry, cur_node._left)
      elif entry > cur_node._entry:
         if cur_node._right is None:
            cur_node._right = bn(entry)
         else:
            self._add_rec(entry, cur_node._right)

   def add(self, entry):
      '''Adds an entry to the tree.'''
      if self._root is None:
         self._root = bn(entry)
      else:
         self._add_rec(entry, self._root)

   #   _function = hidden/private recursive method
   def _rec_search(self, target, cur_node):
      '''Searches a binary tree for a given target.'''
      if cur_node is None: # if pokemon does not exist
         return None
      elif cur_node._entry._number == target: # if pokemon found
         return cur_node # return pokemon
      else:
         # recursive case by searching left subtree and right subtree
         if target < cur_node._entry._number:
            return self._rec_search(target, cur_node._left)
         else:
            return self._rec_search(target, cur_node._right)

   def search(self, target):
      '''Searches for target starting from root of binary tree.'''
      my_pokemon = self._rec_search(target, self._root)
      if my_pokemon is not None: # if pokemon exists
         return my_pokemon # return pokemon
      else: # if pokemon does not exist
         return None # return none

   def _in_order_rec(self, cur_node): # lst, print, rst
      '''Recursively implements in order traversal.'''
      if cur_node is not None:
         self._in_order_rec(cur_node._left)
         print(cur_node._entry)
         self._in_order_rec(cur_node._right)

   def _pre_order_rec(self, cur_node): # print, lst, rst
      '''Recursively implements pre order traversal.'''
      if cur_node is not None:
         print(cur_node._entry)
         self._pre_order_rec(cur_node._left)
         self._pre_order_rec(cur_node._right)

   def _post_order_rec(self, cur_node): # lst, rst, print
      '''Recursively implements post order traversal.'''
      if cur_node is not None:
         self._post_order_rec(cur_node._left)
         self._post_order_rec(cur_node._right)
         print(cur_node._entry)

   def print_in_order(self, cur_node):
      '''Prints each pokemon via in order traversal.'''
      if self._root is not None:
         self._in_order_rec(self._root)

   def print_pre_order(self, cur_node):
      '''Prints each pokemon via pre order traversal.'''
      if self._root is not None:
         self._pre_order_rec(self._root)

   def print_post_order(self, cur_node):
      '''Prints each pokemon via post order traversal.'''
      if self._root is not None:
         self._post_order_rec(self._root)
