class Cat:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.kids = []

    def getname(self):
        return self.name

    def getparent(self):
        return self.parent

    def makechild(self):
        kid = Cat((self.name + "-" + str(len(self.kids))), parent=self.name)
        self.kids.append(kid)
        return kid

    def getchildren(self):
        return self.kids

    def __repr__(self):
        return "<cat " + self.getname() + ">"

    def __str__(self):
        return "<cat " + self.getname() + ">"


c = Cat("Pepsi")
print(c.getname())
c2 = c.makechild()
print(c2)
print(c2.getparent())
print(c.getchildren())

c2.makechild()
c2.makechild()
c2.makechild()

print(c2.getchildren())
