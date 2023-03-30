'''
Author: Drew Meyer
KUID: 3020061
Date: 3/6/23
Lab: Lab 6
Last Accessed: 3/26/23
Purpose: Driver file responsible for file I/O.
'''

from flood import Flood

class Executive:

   def __init__(self, input_file): # initialize executive class
      self._input_file = input_file

   def run(self):
      '''Runs main and handles file I/O.'''
      input_file = open(self._input_file, "r") # open input in read mode

      my_flood = Flood() # initialize flood class

      lines = input_file.readlines() # create list of lines
      temp_line = lines[0]

      my_map = lines[2: len(lines)] # represents map
      my_flood._map = my_map # initialize map

      try:
         start_pos = (int(temp_line[0]), int(temp_line[2])) # obtain starting position
         my_flood._row = start_pos[0]
         my_flood._col = start_pos[1]

         my_flood_row = len(my_flood._map)
         my_flood_col = len(my_flood._map[0].strip('\n')) # strip newline

         print(f"Size: {my_flood_row},{my_flood_col}") # formatted print
         print(f"Starting Position: {start_pos[0]},{start_pos[1]}")
      except:
         print("Invalid starting position.")

      my_water_count = lines[1].strip()
      my_flood._water_count = int(my_water_count) # obtain water count

      my_flood.advance_flood(my_flood._row, my_flood._col)
      my_flood.get_map()

      if my_flood._water_count <= 0:
         print("Flood ran out of water.")
      else:
         print("Flood complete.")
