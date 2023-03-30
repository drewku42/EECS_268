'''
Author: Drew Meyer
KUID: 3020061
Date: 1/30/23
Lab: Lab 2
Last Accessed: 2/3/23
Purpose: Responsible for I/O and user interaction.
'''

from process import Process
from function import Function

class Executive:

   def __init__(self, input_file): # initialize executive class
      self._input_file = input_file

   def run(self):
      user_input = open(self._input_file, "r") # open user file in read mode

      user_input = user_input.readlines()
      start = user_input[0].split()
      my_process = Process(start[1]) # intitialize process
      my_process.start() # print to user

      for i in user_input[1:]: # for each call after start of process...
         i = i.split() # split each line into list
         if i[0] == "CALL":
            my_function = Function(i[1], i[2]) # initialize function
            my_process.call(my_function) # push function onto call stack, print to user
         elif i[0] == "RETURN":
            my_process.my_return()
         elif i[0] == "RAISE":
            my_process.my_raise()
