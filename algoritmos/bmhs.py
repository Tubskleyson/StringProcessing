from sys import argv

def bmhs(P, T):

    """
    Realiza a busca pelo método Boyer-Moore-Horspool-Sunday
    :param str T:
    :param str P:
    :return int[]:
    """

    m = len(P)
    n = len(T)

    r, d = [], [ m + 1 for _ in range(1000)]

    for i in range(m): d[ ord(P[i]) ] = m - i

    i = m - 1

    while i < n-1:

        k, j = i, m - 1

        while j >= 0 and T[k] == P[j]:

            j -= 1
            k -= 1

        if j < 0: r.append(k+1)

        i += d[ ord(T[ i + 1 ]) ]

    return  r

if __name__ == "__main__":

    if len(argv) > 2:

        p = argv[1]
        t = open(argv[2]).read()

        print(bmhs(p,t))