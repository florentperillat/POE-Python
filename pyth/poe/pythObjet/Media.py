class Publisher:

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Author:

    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName= firstName
        self.lastName = lastName

import abc
class Media(metaclass=abc.ABCMeta):

    def __init__(self, id, title, price):
        self.id = id
        self.price = price
        self.title = title
        self.publisher = None
        self.authors = []

    @abc.abstractmethod
    def netPrice(self):...

class Book(Media):

    def __init__(self, id, title, price, nbPage = 0):
        super().__init__(id,title,price)
        self.nbPage = nbPage

    def netPrice(self):
        return self.price * 1.05 * 0.95 + 0.01

class Cd(Media):

    def __init__(self, id, title, price, nbTrack = 0):
        super().__init__(id,title,price)
        self.nbTrack = nbTrack

    def netPrice(self):
        return self.price * 1.05 * 0.95 + 0.01

class CartRow: ##CartRow = MediaRow dans mon programme Java, avec un meilleur titre

    def __init__(self, media = None):
        self.media = media
        self.quantity = 1

    def increment(self):
        self.quantity += 1 ##pas de ++ en python

    def decrement(self):
        self.quantity -= 1 ##pas de -- en python

class Cart:

    def __init__(self):
        self.cartRows = []

    def isMediaInCart(self, media):
        # res = None
        # for row in self.cartRows:
        #     if media == row.media:
        #         res = row
        #         break
        # return res
        l = [row.media for row in self.cartRows if row.media == media]
        if len(l) == 0:
            return None
        else:
            return l[0]

    def add(self, media):
        row = self.isMediaInCart(media)
        if row == None:
            row = CartRow(media)
            self.cartRows.append(row)
        else:
            row.increment()

    def remove(self, media):
        row = self.isMediaInCart()
        if row.quantity > 1:
            row.decrement()
        else:
            self.cartRows.remove(row)

    def totalNetPrice(self):
        # res = 0
        # for row in self.cartRows:
        #     res += row.media.netPrice()
        # return res // Equivalent à :
        return sum([row.media.netPrice() for row in self.cartRow])

if __name__ == '__main__':
    p1 = Publisher(0,"ENI")
    a1 = Author(1,"Cyril","Vincent")
    b = Book(2, "Python", 10)
    b.publisher = p1
    b.authors.append(a1)
    print(b.netPrice())
    cart = Cart()
    cart.add(b)
    cart.add(b)
    cart.add(Cd(0,"Johnny",10))
    print(cart.totalNetPrice())