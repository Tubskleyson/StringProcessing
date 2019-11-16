"""
Algoritmos de casamento exato
"""

def forca_bruta(T, n, P, m):

    """
    Realiza a busca pelo método de força brura
    :param str T:
    :param int n:
    :param str P:
    :param int m:
    :return int[]:
    """

    r = []

    for i in range(n - m + 1):

        k, j = 0, 0

        while j < m and T[k] == P[k]:

            j += 1
            k += 1

        if j == m: r.append(i)

    return r


def bmh(T, n, P, m):

    """
    Realiza a busca pelo método Boyer-Moore-Horspool
    :param str T:
    :param int n:
    :param str P:
    :param int m:
    :return int[]:
    """

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

def bmhs(T, n, P, m):

    """
    Realiza a busca pelo método Boyer-Moore-Horspool-Sunday
    :param str T:
    :param int n:
    :param str P:
    :param int m:
    :return int[]:
    """

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
