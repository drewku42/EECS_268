'''
Author: Drew Meyer
KUID: 3020061
Date: 2/13/23
Lab: Lab 4
Last Accessed: 2/21/23
Purpose: Executive file which handles user input and I/O
'''

from webbrowser import WebBrowser

class Executive:

   def __init__(self, input_file): # initialize executive class
      self._input_file = input_file

   def run(self):
      '''Runs main program, handles file I/O.'''
      mybrowser = WebBrowser() # initialize web browser
      input_file = open(self._input_file, "r") # open input in read mode

      for line in input_file: # for line in file
         line = line.split()
         if line[0] == 'NAVIGATE':
            mybrowser.navigate_to(line[1])
         elif line[0] == 'BACK':
            mybrowser.back()
         elif line[0] == 'FORWARD':
            mybrowser.forward()
         elif line[0] == 'HISTORY':
            mybrowser.history()

