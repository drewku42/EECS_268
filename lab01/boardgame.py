'''
Author: Drew Meyer
Student ID: 3020061
Date Created: 1/23/23
Lab: Lab #1
Last Accessed: 1/30/23
Purpose: Creates object representing a board game with associated parameters.
'''

class BoardGame:

   def __init__(self,name,year,GR,PR,MP,MT):
      '''Initializes BoardGame class. Paremters: name, year, Gibbons Rating, Peoples Rating, min players, max playtime'''
      self._name = name
      self._year = year
      self._GR = GR
      self._PR = PR
      self._MP = MP
      self._MT = MT

   def __str__(self):
      '''Returns string representation of BoardGame class with associated parameters.'''
      string =  f'{self._name} ({self._year}) [GR={self._GR},PR={self._PR},MP={self._MP},MT={self._MT}]'
      return string

   def __lt__(self,other):
      return self._GR < other._GR

   def __gt__(self,other):
      return self._GR > other._GR

   def __eq__(self,other):
      return self._GR == other._GR

   def is_year(self, year):
      '''Returns true if a boardgame's year is equal given year.'''
      if int(self._year) == year:
         return True

   def is_time(self, time):
      '''Returns true if a boardgame's time is less than or equal to given time.'''
      if int(self._MT) <= time:
         return True

   def get_GR(self):
      '''Gets and returns boardgame's Gibbons Rating.'''
      return self._GR

   def get_PR(self):
      '''Gets and returns boardgame's Public Rating.'''
      return self._PR

   def threshold(self):
      '''Returns the absolute value of the difference GR and PR.'''
      difference = float(self._GR) - float(self._PR)
      threshold = abs(difference)
      return threshold
