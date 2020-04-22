from sympy import Symbol,pprint
import sympy as sym
import sympy.plotting as syp
import matplotlib.pyplot as plt

a = Symbol('a')
lam =Symbol('lambda' )

deger1 = ((lam**a)*sym.exp(-lam))
deger2 = sym.factorial(a)

ols = deger1/deger2
pprint(ols)

syp.plot(ols.subs({lam:5}),(a,0,10),title="Poisson Distribution")
plt.show()

a_degeri=[]
b_degeri=[]
for deger in range(12):
    y=ols.subs({lam:5,a:deger}).evalf()
    b_deger.append(b)
    a_deger.append(deger)
plt.plot(a_deger, b_deger)
plt.show()
"""
Ad Soyad : Halil İbrahim Türkmenoğlu
Numara : 180401006
180401006 % 4 Değerinin Sonucu = 2
GİTHUB: github.com/halillibo

"""
