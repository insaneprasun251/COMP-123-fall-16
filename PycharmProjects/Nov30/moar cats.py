class Cat:
    def __init__(self, name, color, parent=None):
        self.name = name
        self.parent = parent
        self.kids = []
        self.color = color

    def getname(self):
        return self.name

    def getparent(self):
        return self.parent

    def getcolor(self):
        return self.color

    def makechild(self):
        kid = Cat((self.name + "-" + str(len(self.kids))), self.color, parent=self)
        self.kids.append(kid)
        return kid

    def getchildren(self):
        return self.kids

    def countancestors(self):
        if self.parent == None:
            return 0
        else:
            return 1 + self.parent.countancestors()

    def countdescendants(self):
        if len(self.kids) == 0:
            return 0
        else:
            descendants = 0
            for kid in self.kids:
                descendants = descendants + 1 + kid.countdescendants()
            return descendants
    
    # def longestdescendantname(self):
    #     longname = [""]
    #     for kid in self.kids:
    #         if len(kid.name) > len(longname[0]):
    #             longname[0] = kid.getname()
    #             
                

    def __repr__(self):
        return "<cat " + self.getname() + ">"

    def __str__(self):
        return "<cat " + self.getname() + ">"


c = Cat("Nermal", "orange")
c2 = c.makechild()
c3e = c.makechild()
c4 = c2.makechild()
c567 = c3e.makechild()
c666666 = c567.makechild()

print(c.countdescendants())
print(c.kids)
