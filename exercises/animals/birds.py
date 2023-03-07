"""
Module contaning the birds class definition
"""

class Birds:
    
    def __init__(self):
        self.members = ['Sparrow', 'Crow', 'Robin', 'Duck', 'Eagle', 'Hawk']

    def printMembers(self):
        print('Members in the Birds class:')
        for member in self.members:
            print(' \t%s ' % member)


