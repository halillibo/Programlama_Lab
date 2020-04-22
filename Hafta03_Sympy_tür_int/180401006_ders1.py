from sympy import Symbol, Limit
import pprint
t = Symbol('t')
Pt = 5 * t ** 2 + 2 * t + 8
t1 = Symbol('t1')
delta_t = Symbol('delta_t')
Pt1 = Pt.subs({t: t1})
Pt1_delta = Pt.subs({t: t1 + delta_t})
print(Limit((Pt1_delta - St1) / delta_t, delta_t, 0).doit())
