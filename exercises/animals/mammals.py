"""
Contain the mammals class definition.
"""

class Mammals:
    def __init__(self):
        self.members = ['Cat', 'Dog', 'Bear', 'Wolf', 'Sheep', 
                        'Pangolin', 'Panda']

    def printMembers(self):
        print('Members of the Mammals class:')
        for member in self.members:
            print(' \t%s '  % member)
