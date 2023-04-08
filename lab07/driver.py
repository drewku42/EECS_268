'''
Author: Drew Meyer
KUID: 3020061
Date: 3/27/23
Lab: Lab 7
Last Accessed: 3/27/23
Purpose: Handles file I/O, starts main program.
'''
from executive import Executive

def main():
   file_name = input("Enter the name of the input file: ")
   my_exec = Executive(file_name)
   my_exec.run()

if __name__ == "__main__":
   main()
