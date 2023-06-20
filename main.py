from KiK.LinearAlgebra import *
from KiK.ElipticCurves import *


# /////////////////// modulo calculator ///////////////////
number = 81 - 1 - 14
n = 31

if False:
    calc_modulo(number, n, True)

# /////////////////////////////////////////////////////////

# ///////////////////// modulo inverse ////////////////////
number = 79
n = 3220

if False:
    modulo_inverse(number, n, True)

# /////////////////////////////////////////////////////////

# //////////////////// primitive roots ////////////////////
p = 101

if False:
    print(calc_primitive_roots(p))

# /////////////////////////////////////////////////////////

# ////////////////////////// phi //////////////////////////
n = 16

if False:
    print("phi(", n, ") =", phi(n))

# /////////////////////////////////////////////////////////

# ///////////////// double point on curve /////////////////
# point
point = [3, 5]

# curve
a = 1
p = 11

if True:
    xr, yr, s = double_point_on_curve(point, a, p)
    print("R = 2P = (", xr, ", ", yr, ")", sep="")
    print("s =", s, "mod", p)

# /////////////////////////////////////////////////////////

# ///////////////// double point on curve /////////////////
# point
point_p = [8, 9]
point_q = [9, 4]

# curve
p = 13

if False:
    xr, yr, s = add_points_on_curve(point_p, point_q, p)
    print("P + Q = (", xr, ", ", yr, ")", sep="")
    print("s =", s, "mod", p)

# /////////////////////////////////////////////////////////
