from sympy import totient


def calc_modulo(number, modulo, show_progress=False):
    result = number % modulo
    if show_progress:
        print(number, " mod", modulo, " = ", result, sep="")
    return result


def gca(a, b, q=[], r=[], bigger=[], lower=[], show_progress=False):
    if a > b:
        quantity = a // b
        rest = a - quantity * b
        if show_progress:
            print(a, "-", quantity, "*", b, "=", rest)
        r.append(rest)
        q.append(quantity)
        bigger.append(a)
        lower.append(b)
        if rest == 0:
            return b, q, r, bigger, lower
        else:
            return gca(b, rest, q, r, bigger, lower, show_progress)
    else:
        quantity = b // a
        rest = b - quantity * a
        if show_progress:
            print(b, "-", quantity, "*", a, "=", rest)
        r.append(rest)
        q.append(quantity)
        bigger.append(b)
        lower.append(a)
        if rest == 0:
            return a, q, r, bigger, lower
        else:
            return gca(a, rest, q, r, bigger, lower, show_progress)


def modulo_inverse(number, n, show_progress=False):
    # gca
    if show_progress:
        print("----GCA----")
    gca_result, q, r, bigger, lower = gca(number, n, show_progress=show_progress)
    
    if show_progress:
        print("GCA =", gca_result)

    #
    if gca_result != 1:
        print("There is no inverse")
        return
    else:
        if show_progress:
            print("----Inverse----")
        # initial values
        r = list(reversed(r))[1:]
        q = list(reversed(q))[1:]
        bigger = list(reversed(bigger))[1:]
        lower = list(reversed(lower))[1:]

        # current values
        r_current = r[0]
        q_lower_current = -q[0]
        q_bigger_current = 1
        bigger_current = bigger[0]
        lower_current = lower[0]
        if show_progress:
            print(r_current, "=", q_bigger_current, "*", bigger_current,
                  "+", q_lower_current, "*", lower_current)
        i = 1
        # loop
        while bigger_current != n:
            if show_progress:
                print("=", q_bigger_current, "*",  bigger_current,
                      "+", q_lower_current, "*", "(", bigger[i], "+",
                      -q[i], "*", lower[i], ")")
            temp = q_bigger_current
            q_bigger_current = q_lower_current
            lower_current = bigger_current
            bigger_current = bigger[i]
            q_lower_current = q_lower_current * (-q[i]) + temp
            if show_progress:
                print("=", q_bigger_current, "*", bigger_current,
                      "+", q_lower_current, "*", lower_current)
            i += 1
        if show_progress:
            print("----Result-----")
            print(number, "^-1 =", q_lower_current, "=", q_lower_current % n, "mod", n)
        return q_lower_current % n


def calc_primitive_roots(p):
    all_numbers = [i for i in range(1, p)]
    roots = list()

    for i in range(2, p):
        temp_list = list()
        for j in range(1, p):
            temp_list.append((i ** j) % p)
        temp_list.sort()
        if temp_list == all_numbers:
            roots.append(i)
    return roots


def phi(n):
    return totient(n)
