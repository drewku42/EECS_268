'''
Author: Drew Meyer
KUID: 3020061
Date: 3/6/23
Lab: Lab 6
Last Accessed: 3/12/23
Purpose: Driver file responsible for starting program.
'''

from executive import Executive

def main():
   file_name = input("Enter the name of the input file: ")
   my_exec = Executive(file_name)
   my_exec.run()

if __name__ == "__main__":
   main()
