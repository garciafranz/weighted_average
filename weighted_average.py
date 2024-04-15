RATIO = (2.1,)

def weighted_average(xs):
    num = 0
    den = 0
    for p in range(len(xs)):
        num += xs[p] * RATIO[0] ** p
        den += RATIO[0] ** p
    return 1.0 * num / den

def main():
    return

if '__main__' == __name__:
    main()
