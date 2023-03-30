'''
Author: Drew Meyer
KUID: 3020061
Date: 1/30/23
Lab: Lab 2
Last Accessed: 2/2/23
Purpose: Main executable.
'''

from executive import Executive

def main():
   file_name = input("Enter name of input file: ")
   my_exec = Executive(file_name)
   my_exec.run()

if __name__ == "__main__":
   main()
