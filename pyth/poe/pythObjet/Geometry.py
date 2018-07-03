class Point:



    def __init__(self, x=0, y=0):

        self.x = x

        self.y = y



    def __repr__(self): # = toString()

        return f"({self.x},{self.y})"





class Rectangle: # Pas de public et private



    # Constructeur

    def __init__(self, width=0, height=0, origin=Point()): # self = this mais obligatoire
        self.width = width
        self.height = height # Pas déclaration
        self.origin = origin

    def surface(self):
        return self.width * self.width # self est obligatoire

# toutes les classes dans un ou plusieurs fichiers
class Carre(Rectangle): # () = extends

    def __init__(self, cote):
        super().__init__(cote,cote) # On doit ajouter ().__init__

class VintageVideoGame:

    def __init__(self):
        self.rectangles = []

if __name__ == '__main__':
    r1 = Rectangle(2,3,Point(2,-1)) # pas de new
    print(r1.surface())
    c1 = Carre(2)
    print(r1.surface())
    p1 = Point(2,-1)
    p1 = Point(y=-1,x=2)
    r1.origin = p1
    vvg = VintageVideoGame()
    vvg.rectangles.append(r1)
    vvg.rectangles.append(c1)