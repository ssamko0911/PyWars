# https://www.codewars.com/kata/55b75fcf67e558d3750000a3/train/python

class Block(object):
    def __init__(self, params: list):
        self.width, self.length, self.height = params

    def get_width(self)->int:
        return self.width

    def get_length(self)->int:
        return self.length

    def get_height(self)->int:
        return self.height

    def get_volume(self)->int:
        return self.width * self.length * self.height

    def get_surface_area(self)->int:
        return 2 * ((self.length * self.width) + (self.width * self.height) + (self.length * self.height))
