'''
Author: Drew Meyer
KUID: 3020061
Date: 4/2/23
Lab: Lab 7
Last Accessed: 4/3/23
Purpose: Responsible for receiving input and implementing binary tree.
'''

from binarytree import BinaryTree as bt
from pokemon import Pokemon

class Executive:

   def __init__(self, input_file):
      self._input_file = input_file

   def run(self):
      user_input = open(self._input_file, "r")

      my_bt = bt() # initialize binary tree

      for i in user_input:
         i = i.split()
         my_pokemon = Pokemon(i[0], i[1], i[2])
         my_bt.add(my_pokemon) # add each pokemon to the tree

      running = True

      while running:

         print("1) Search\n2) Add\n3) Print\n4) Quit\n")
         my_input = int(input("Select an option: \n"))

         if my_input == 1:
            user_num = int(input("Search a number: "))
            found = my_bt.search(user_num)
            if found is not None:
               print(f"Pokemon found!\n{found._entry} \n")
            else:
               print("Pokemon not found. \n")

         elif my_input == 2:
            new_us = input("Enter new US name: ")
            new_num = input("Enter new number: ")
            new_jp = input("Enter new JP name: ")
            try:
               new_mon = Pokemon(new_us, new_num, new_jp)
               my_bt.add(new_mon)
               print(f"The following pokemon was added to the pokedex:\n{new_mon}\n")
            except:
               raise RuntimeError("Pokemon already in tree.")

         elif my_input == 3:
         # print should give three options for in order, pre order, post order
            user_choice = int(input("Select: 1 > pre-order, 2 > in-order, 3 > post-order: \n"))
            if user_choice == 1: # pre-order = vist, lst, rst
               print("Printing in pre order:\n")
               my_bt.print_pre_order(my_bt._root)
            elif user_choice == 2: # in-order = lst, visit, rst
               print("Printing in order:\n")
               my_bt.print_in_order(my_bt._root)
            elif user_choice == 3: # post-order = lst, rst, visit
               print("Printing in post order:\n")
               my_bt.print_post_order(my_bt._root)
            else:
               print("Please input either 1, 2 or 3. \n")

         elif my_input == 4:
            running = False
            print("Exiting Pokedex... ")
