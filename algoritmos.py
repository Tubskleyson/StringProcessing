"""
Algoritmos de casamento exato
"""

def forca_bruta(T, P):

    """
    Realiza a busca pelo método de força brura
    :param str T:
    :param str P:
    :return int[]:
    """

    m = len(P)
    n = len(T)

    r = []

    for i in range(n - m + 1):

        k, j = 0, 0

        while j < m and T[k] == P[k]:

            j += 1
            k += 1

        if j == m: r.append(i)

    return r


def bmh(T, P):

    """
    Realiza a busca pelo método Boyer-Moore-Horspool
    :param str T:
    :param str P:
    :return int[]:
    """

    m = len(P)
    n = len(T)

    r, d = [], [m for _ in range(256)]

    for i in range(m-1): d[ ord(P[i]) ] = m - i - 1

    i = m - 1

    while i < n:

        k, j = i, m-1

        while j >= 0 and T[k] == P[j]:

            j -= 1
            k -= 1

        if j < 0: r.append(k+1)

        i += d[ ord(T[i]) ]

    return r

def bmhs(T, P):

    """
    Realiza a busca pelo método Boyer-Moore-Horspool-Sunday
    :param str T:
    :param str P:
    :return int[]:
    """

    m = len(P)
    n = len(T)

    r, d = [], [ m + 1 for _ in range(256)]

    for i in range(m): d[ ord(P[i]) ] = m - i

    i = m - 1

    while i < n:

        k, j = i, m - 1

        while j >= 0 and T[k] == P[j]:

            j -= 1
            k -= 1

        if j < 0: r.append(k+1)

        i += d[ ord(T[ i + 1 ]) ]

    return  r


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

    alf = []| 2**(m-1)
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

def shift_and_aprox(P, T, k):

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


