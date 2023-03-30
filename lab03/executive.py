'''
Author: Drew Meyer
KUID: 3020061
Date: 2/6/23
Lab: Lab 3
Last Accessed: 2/13/23
Purpose: Responsible for I/O and user interaction.
'''

from process import Process
from function import Function
from queue import Queue

class Executive:

   def __init__(self, input_file): # initialize executive class
      self._input_file = input_file

   def run(self):
      schedule = Queue() # intiailize schedule
      user_input = open(self._input_file, "r") # open user file in read mode

      lines = user_input.readlines() # create list of lines

      for line in lines: # for each call after start of process...
         temp_lines = line.split() # split line into list of words

         if temp_lines[0] == "START":
            my_process = Process(temp_lines[1]) # create process
            schedule.enqueue(my_process) # add process to queue

         elif temp_lines[0] == "CALL":
            '''Front of queue calls, then dequeued.'''
            my_function = Function(temp_lines[1], temp_lines[2]) # initialize function
            current_process = schedule.peek_front() # obtain current process
            current_process.call(my_function) # call current_process
            schedule.dequeue()

         elif temp_lines[0] == "RETURN":
            cur_proc = schedule._front.entry # track current process
            print(f"{cur_proc} returns from main.")
            cur_proc.my_return()

         elif temp_lines[0] == "RAISE":
            schedule._front.my_raise()
