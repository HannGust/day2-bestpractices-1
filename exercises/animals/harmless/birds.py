"""
Module contaning the harmless Birds class definition
"""

class Birds:
    
    def __init__(self):
        self.members = ['Sparrow', 'Crow', 'Robin', 'Duck']

    def printMembers(self):
        print('Members in the harmless Birds class:')
        for member in self.members:
            print(' \t%s ' % member)


