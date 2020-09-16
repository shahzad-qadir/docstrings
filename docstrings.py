#!/home/python/MachineLearning/DocStrings/venv/bin/python3

class Square:
    """ This class takes a number returns square of the same number"""
    def __init__(self, number):
        self.number = number
    def get_square(self):
        """ Method squares the numbers received as input while creating the class"""
        return number * number


print(Square.get_square.__doc__)
