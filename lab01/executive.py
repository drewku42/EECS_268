'''
Author: Drew Meyer
Student ID: 3020061
Date Created: 1/23/23
Lab: Lab #1
Last Accessed: 1/23/23
Purpose: Executive class which handles I/O and creates a list of board games.
         Manages user navigation.
'''
from boardgame import BoardGame

class Executive:

   def __init__(self, input_file):
      '''Initializes Executive class with single parameter of input file'''
      self.input_file = input_file

   def run(self):
      '''Handles files I/O and user interaction.'''
      boardgames = [] # create list to store boardgames

      user_file = open(self.input_file, 'r') # open input file in read mode

      for line in user_file: # for line in file
         list = line.split() # split each line into a list of elements
         my_bg = BoardGame(list[0], list[3], list[1], list[2], list[4], list[5]) # assign each element to the appropriate boardgame parameter
         boardgames.append(my_bg) # add each intialization of BoardGame to list of boardgames

      running = True # loop control variable

      while running:
         print("Select an option:")
         user_input = int(input("1) Print by GR\n2) Print by Year\n3) Game time?\n4) People VS Gibbons\n5) Ranking\n6) Quit\n"))

         if user_input == 1:
            boardgames.sort(reverse=True)
            for game in boardgames: # print sorted list by GR, reverse since highest to lowest
               print(game)

         elif user_input == 2:
            user_year = int(input("What year would you like to search for?: "))
            print(f"The following boardgames were made in the year {user_year}.\n")
            for game in boardgames: # if board game matches user year, print board game
               if game.is_year(user_year):
                  print(game)

         elif user_input == 3:
            user_time = int(input("Enter a time: "))
            print(f"The following boardgames may be played in {user_time} minutes or less. \n")
            for game in boardgames:
               if game.is_time(user_time):
                  print(game)

         elif user_input == 4:
            user_num = float(input("Enter threshold for games you would like to see: \n"))
            for game in boardgames:
               if user_num <= game.threshold():
                  print(game)

         elif user_input == 5:
            user_rating = float(input("Enter a rating: "))
            print(f"The following games have a Gibbons Rating of {user_rating} or better.\n")
            for game in boardgames:
               if float(game.get_GR()) >= user_rating:
                  print(game)

         elif user_input == 6:
            running = False
            print("Exiting program... ")
