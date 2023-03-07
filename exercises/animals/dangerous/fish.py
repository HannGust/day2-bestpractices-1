"""
Module contanint the dangerous Fish class definition.
"""

class Fish:
    def __init__(self):
        self.members = ['Great White Shark', 'Hammerhead Shark', 'Pufferfish']

    def printMembers(self):
        print('Members in the dangerous Fish class:')
        for member in self.members:
            print(' \t%s ' % member)

