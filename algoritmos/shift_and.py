from sys import argv

def shift_and(P, T):

    """
    Realiza a busca por meio de shift-and exato
    :param str P:
    :param str T:
    :return int[]:
    """

    r = []

    m = len(P)
    n = len(T)

    alf = []
    M = {}

    for i in T:

        if i not in alf: alf.append(i)

    for c in alf: M[c] = 0

    for j in range(m):
        M[P[j]] = M[P[j]] | 2**(m-j-1)


    R = 0

    for i in range(n):

        R = ((R >> 1) | 2 ** (m-1)) & M[T[i]]

        if R & 1 != 0 :r.append(i - m + 1)

    return r

if len(argv) > 2:

    p = argv[1]
    t = open(argv[2]).read()

    print(shift_and(p,t))