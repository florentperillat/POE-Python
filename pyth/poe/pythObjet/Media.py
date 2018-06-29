class Media:

    def __init__ (self, id, title, price):
        self.id=id
        self.title=title
        self.price=price

    def __repr__(self): # = toString()
        return f"{self.id} : {self.title} | {self.price})"

    def netPrice(self):
        return self.price*1.2

class Book(Media):

    def __init__ (self, id, title, price):
        super().__init__(id, title, price)

class Dvd(Media):

    def __init__ (self, id, title, price):
        super().__init__(id, title, price)

class Cd(Media):


    def __init__ (self, id, title, price):
        super().__init__(id, title, price)