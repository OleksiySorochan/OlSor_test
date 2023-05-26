class Paralilogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        w = self.width
        l = self.length
        s_pal = (l * w) / 3 * 2
        return s_pal

class Square(Paralilogram):
    def get_area(self):
        w = self.width
        l = self.length
        s_sq = w * l
        return s_sq

pal = Paralilogram(25, 6)
print(pal.get_area())
sq = Square(5,5)
print(sq.get_area())
