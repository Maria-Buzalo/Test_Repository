x = float(input())
if x < 0 :
    print("f(x) =", -x)
elif x == 0:
    print("f(x) = 0")
elif x > 0 and x < 2:
    print("f(x) =", x**2)
elif x > 2 or x == 2:
    print("f(x) = 4")