"""
Module contaning the dangerous Birds class definition
"""

class Birds:
    
    def __init__(self):
        self.members = ['Eagle', 'Hawk']

    def printMembers(self):
        print('Members in the dangerous Birds class:')
        for member in self.members:
            print(' \t%s ' % member)


