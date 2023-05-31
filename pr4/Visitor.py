class Visitor(object):
    """Посетитель"""

    def draw(self, theatre):
        methods = {
            Bolshoi: self.draw_Bolshoi,
            Maly: self.draw_Maly,
            Art: self.draw_Art,
            Sovremennik: self.draw_Sovremennik,
        }
        draw = methods.get(type(theatre), self.draw_unknown)
        draw(theatre)

    def draw_Bolshoi(self, theatre):
        print('Bolshoi Theatre')

    def draw_Maly(self, theatre):
        print('Maly Theatre')

    def draw_Art(self, theatre):
        print('Moscow Art Theatre')

    def draw_Sovremennik(self, theatre):
        print('Sovremennik')

    def draw_unknown(self, theatre):
        print('Moscow theaters')

class Theatre(object):
    """Теарт"""

    def draw(self, visitor):
        visitor.draw(self)


class Bolshoi(Theatre):
    """Большой"""


class Maly(Theatre):
    """Малый"""


class Art(Theatre):
    """Арт"""


class Sovremennik(Theatre):
    """Современник"""

visitor = Visitor()

one = Bolshoi()
one.draw(visitor)

two = Maly()
two.draw(visitor)

three = Art()
three.draw(visitor)

four = Sovremennik()
four.draw(visitor)
