'''
Author: Drew Meyer
KUID: 3020061
Date: 3/6/23
Lab: Lab 6
Last Accessed: 3/26/23
Purpose: File which simulates water flow based on orthogonal movement.
'''

class Flood:

   def __init__(self):
      self._row = 0 # tracks current row
      self._col = 0 # tracks current column
      self._water_count = 0 # total amount of water
      self._map = map # map to be traversed

   def get_dimensions(self):
      '''Returns dimensions of map.'''
      dimensions = [len(self._map), len(self._map[0])]
      return dimensions

   def mark_position(self, row, col):
      '''Mark current position, decrement water count by 1.'''
      self._map[row] = list(self._map[row])
      self._map[row][col] = '~'
      self._map[row] = ''.join(self._map[row])
      self._row = row
      self._col = col
      self._water_count -= 1 # decrement water count

   def is_lowground(self, row, col):
      '''Checks to see if space is lowground.'''
      if self._map[row][col] == ' ': # if lowground
         return True
      else:
         return False

   def is_valid_move(self, row, col):
      '''Checks to see if the next move is valid'''
      max_row = self.get_dimensions()[0]
      max_col = self.get_dimensions()[1]
      if row < 0 or row >= max_row or col < 0 or col >= max_col:
         return False
      if self._map[row][col] == 'H':
         return False
      return True # if all conditions valid, return True

   def __str__(self):
      '''Returns human readable string format.'''
      return f'Flood({self._row}, {self._col}, {self._water_count})'

   def get_map(self):
      for i in self._map:
         print(i.strip('\n'))

   def advance_flood(self, row, col):
      '''Initiates map traversal.'''
      if not self.is_valid_move(row, col) or self._water_count <= 0:
         print("Flood ran out of water or invalid move.")
         return

      # if low ground...
      if self.is_lowground(row, col):
         self.mark_position(row, col)

         # look up
         if self.is_valid_move(row-1, col):
            flood_up = self.advance_flood(row-1, col)

         # look right
         if self.is_valid_move(row, col+1):
            flood_right = self.advance_flood(row, col+1)

         # look down
         if self.is_valid_move(row+1, col):
            flood_down = self.advance_flood(row+1, col)

         # look left
         if self.is_valid_move(row, col-1):
            flood_left = self.advance_flood(row, col-1)
