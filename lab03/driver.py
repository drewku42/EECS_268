'''
Author: Drew Meyer
KUID: 3020061
Date: 2/6/23
Lab: Lab 3
Last Accessed: 2/6/23
Purpose: Main executable.
'''

from executive import Executive

def main():
   file_name = input("Enter name of input file: ")
   my_exec = Executive(file_name)
   my_exec.run()

if __name__ == "__main__":
   main()
