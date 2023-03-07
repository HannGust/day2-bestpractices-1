"""
Module containing the harmless Mammals class definition.
"""

class Mammals:
    def __init__(self):
        self.members = ['Cat', 'Dog', 'Sheep', 'Pangolin', 'Panda']

    def printMembers(self):
        print('Members of the harmless Mammals class:')
        for member in self.members:
            print(' \t%s '  % member)
