#  x = lambda y, *z, **a: (y, z, sorted(a.items()))
#  
#  print x(1, 2, 4, 5, 2, k=3, r=4, l=2)

(_10, _6, _7, _8, _9) = (3, 1, 2, 4, 5)
(_5,) = (sorted,)
_1 = lambda _2, *_3, **_4: (_2, _3, _5(_4.items()))
print _1(_6, _7, _8, _9, _7, k=_10, r=_8, l=_7)
(x,) = (_1,)