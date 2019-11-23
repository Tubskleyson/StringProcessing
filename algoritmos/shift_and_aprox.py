from sys import argv

def shift_and_aprox(P, T, k = 2):

    """
    Realiza a busca por meio de shift-and exato
    :param str P:
    :param str T:
    :param int k:
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


    R = [0 for _ in range(k+1)]

    for j in range(k+1):
        exec(f"R[j] = 0b{'1'*j}{'0'*(m-j)}")

    for i in range(n):

        Ra = R[0]

        Rn =  ((Ra >> 1) | 2 **(m-1)) & M[T[i]]

        R[0] = Rn

        for j in range(1,k+1):

            Rn = ((R[j] >> 1) & M[T[i]]) | Ra | ((Ra | Rn) >> 1)

            Ra= R[j]

            R[j] = Rn | 2**(m-1)

        if Rn & 1 != 0 :r.append(i)

    return r

if len(argv) > 2:

    p = argv[1]
    t = open(argv[2]).read()

    print(shift_and_aprox(p,t))