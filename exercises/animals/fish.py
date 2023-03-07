"""
Fish class definition.
"""

class Fish:
    def __init__(self):
        self.members = ['Cod', 'Salmon', 'Great White Shark', 'Tuna', 
                        'Hammerhead Shark', 'Pufferfish', 'Clownfish']

    def printMembers(self):
        print('Members in the Fish class:')
        for member in self.members:
            print(' \t%s ' % member)

