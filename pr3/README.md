# Паттерн Strategy
``` {py}
import random
from abc import ABC, abstractmethod

class Variant(ABC):
    @abstractmethod
    def selection(self) -> None:
        pass

class Paper(Variant):
    def selection(self) -> str:
        return "Бумага"

class Rock(Variant):
    def selection(self) -> str:
        return "Камень"

class Chik(Variant):
    def selection(self) -> str:
        return "Ножницы"

class Spok(Variant):
    def selection(self) -> str:
        return "Спок"

class Zemnovodnoe(Variant):
    def selection(self) -> str:
        return "Ящерица"


class Random(Variant):
    def selection(self) -> str:
        options = ["Бумага", "Камень", "Ножницы", "Спок", "Ящерица"]
        return random.choice(options)

class Game:
    strategy: Variant

    def __init__(self, strategy: Variant = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Random()

    def play(self, sec2) -> None:
        s1 = self.strategy.selection()
        s2 = sec2.strategy.selection()
        if s1 == s2:
            print("Ничья!")


        elif s1 == "Камень":
            if s2 == "Ножницы":
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Бумага"):
                print("Побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("Спок"):
                print("Побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("Ящерица"):
                print("Побеждает первый игрок!", s1, '>', s2)



        elif s1 == "Бумага":
            if s2 == "Ножницы":
                print("Побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("Камень"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Спок"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Ящерица"):
                print("Побеждает второй игрок!", s1, '<', s2)


        elif s1 == "Ножницы":
            if s2 == "Камень":
                print("Побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("Бумага"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Ящерица"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Спок"):
                print("Побеждает второй игрок!", s1, '<', s2)


        elif s1 == "Спок":
            if s2 == "Бумага":
                print("Побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("Камень"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Ножницы"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Ящерица"):
                print("Побеждает второй игрок!", s1, '<', s2)


        elif s1 == "Ящерица":
            if s2 == "Ножницы":
                print("Побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("Бумага"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Спок"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Камень"):
                print("Побеждает второй игрок!", s1, '<', s2)


def playtime(vibor):
    if vibor == "Бумага":
        return Game(Paper())
    elif vibor == "Ножницы":
        return Game(Chik())

    elif vibor == "Камень":
        return Game(Rock())
    elif vibor == "Спок":
        return Game(Spok())
    elif vibor == "Ящерица":
        return Game(Zemnovodnoe())
    elif vibor == "Рандом":
        return Game(Random())

n=1
while n==1:
    print("Первый игрок:\nСделайте выбор: Бумага, Камень, Ножницы, Спок, Ящерица, Рандом")
    vibor=input()
    while vibor not in ("Бумага", "Камень", "Ножницы", "Спок", "Ящерица", "Рандом"):
        print("Повторите ввод")
        vibor=input()
    player1 = playtime(vibor)

    print("Второй игрок:\nСделайте выбор: Бумага, Камень, Ножницы, Спок, Ящерица, Рандом")
    vibor = input()
    while vibor not in ("Бумага", "Камень", "Ножницы", "Спок", "Ящерица", "Рандом"):
        print("Повторите ввод")
        vibor=input()
    player2 = playtime(vibor)
    player1.play(player2)
    print("Хотите повторить? 1-Да")
    n=int(input())
print("Конец! Спасибо за игру!")
``` 

# Паттерн Template method
``` {py}
from abc import ABC, abstractmethod


class Algorithm(ABC):

    def template_method(self):

        self.flagstock()
        self.draw_1()
        self.draw_2()
        self.draw_3()
        self.final()
        self.printer()

    def flagstock(self):
        print("Флагшток нарисован")

    @abstractmethod
    def draw_1(self):
        pass

    @abstractmethod
    def draw_2(self):
        pass

    @abstractmethod
    def draw_3(self):
        pass

    def final(self):
        print('Флаг готов!')

    def printer(self):
        n = 50
        print("-" * n)

class colors:
    def painwhite(self):
        print("Полоса белого цвета нарисована")

    def painred(self):
        print("Полоса красного цвета нарисована")

    def painblue(self):
        print("Полоса синего цвета нарисована")

    def painblack(self):
        print("Полоса черного цвета нарисована")

    def painyel(self):
        print("Полоса желтого цвета нарисована")

class RussianFlag(Algorithm):
    def draw_1(self):
        z = colors()
        z.painwhite()

    def draw_2(self):
        z = colors()
        z.painblue()

    def draw_3(self):
        z = colors()
        z.painred()

    def final(self):
        print('Флаг России готов!')

class Ger(Algorithm):
    def draw_1(self):
        z = colors()
        z.painblack()

    def draw_2(self):
        z = colors()
        z.painred()

    def draw_3(self):
        z = colors()
        z.painyel()


print("Рисуем флаг России")
a=RussianFlag()
a.template_method()



print("Рисуем флаг Германии")
b=Ger()
b.template_method()
```
