'''
Author: Drew Meyer
Student ID: 3020061
Date Created: 1/23/23
Lab: Lab 01
Last Accessed: 1/30/23
Purpose: Program which imports the executive class and runs the main program.
'''

from executive import Executive

def main():
   '''Function which obtains the input file and calls the executive class.'''
   input_file = input('Enter name of input file: ')
   my_exec = Executive(input_file)
   my_exec.run()

if __name__ == '__main__': # runs main function
   main()
