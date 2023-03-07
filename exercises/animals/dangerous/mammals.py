"""
Module containing the dangerous Mammals class definition.
"""

class Mammals:
    def __init__(self):
        self.members = ['Bear', 'Wolf']

    def printMembers(self):
        print('Members of the dangerous Mammals class:')
        for member in self.members:
            print(' \t%s '  % member)
