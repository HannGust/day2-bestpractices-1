"""
Module containing the harmless Fish class definition.
"""

class Fish:
    def __init__(self):
        self.members = ['Cod', 'Salmon', 'Tuna', 'Clownfish']

    def printMembers(self):
        print('Members in the harmless Fish class:')
        for member in self.members:
            print(' \t%s ' % member)

