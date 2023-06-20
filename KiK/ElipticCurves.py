from .LinearAlgebra import modulo_inverse


def add_points_on_curve(point_p, point_q, p):
    # compute s
    y = point_p[1] - point_q[1]
    x = point_p[0] - point_q[0]

    x = x % p
    x = modulo_inverse(x, p)
    s = y * x
    s = s % p

    # xr
    xr = (s ** 2 - point_p[0] - point_q[0])
    xr = xr % p

    # yr
    yr = s * (point_p[0] - xr) - point_p[1]
    yr = yr % p

    #
    return xr, yr, s


def double_point_on_curve(point, a, p):
    # compute s
    x = 3 * point[0]**2 + a
    y = 2 * point[1]
    y = y % p
    y_inverse = modulo_inverse(y, p)
    s = x * y_inverse
    s = s % p

    # compute xr and yr
    xr = s**2 - 2 * point[0]
    xr = xr % p

    yr = s * (point[0] - xr) - point[1]
    yr = yr % p

    # return result
    return xr, yr, s

