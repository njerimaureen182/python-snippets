class Fraction:

    def __init__(self,top,bottom):

        self.num=top
        self.den=bottom

    def __add__(self,otherfraction):

        newnum=self.num*otherfraction.den+self.den*otherfraction.num
        newden=self.den*otherfraction.den

        return Fraction(newnum,newden)

f1=Fraction(1,4)
f2=Fraction(2,3)
f3=f1+f2
print(f3)
