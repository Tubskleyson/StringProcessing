from sys import argv

def bmh(P, T):

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

if __name__ == "__main__":

    if len(argv) > 2:

        p = argv[1]
        t = open(argv[2]).read()

        print(bmh(p,t))