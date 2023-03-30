'''
Author: Drew Meyer
KUID: 3020061
Date: 2/13/23
Lab: Lab 4
Last Accessed: 2/21/23
Purpose: Driver file responsible for starting program.
'''

from executive import Executive

def main():
  file_name = input("Enter the name of the input file: ")
  my_exec = Executive(file_name)
  my_exec.run()

if __name__ == "__main__":
  main()
