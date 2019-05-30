class Fraction:
    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

myf=Fraction(3,5)

print(myf)
print("I ate",myf,"of the pizza I bought.")

