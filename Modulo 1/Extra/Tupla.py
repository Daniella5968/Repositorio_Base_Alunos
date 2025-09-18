tubla=("a","b","c")
tupla=('a','b','c')
print(tubla)

L=[2,7,9,4,0,2,5,10,89,9,11]

for e , x in enumerate(L):
    print("%d X %d = %f" % (x, e, x/e))

for x, e in enumerate(L):
    print("%d X % d= %d" % (x, e, x*e))     

for x, e in enumerate(L):
 print("%d / %d= %d" % (x,e,x-e))

for x, e in enumerate(L):
   print("%d +%d =%d" % (x, e, x+e))