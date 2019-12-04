from sys import argv

def forca_bruta(P, T):
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

        k, j = i, 0

        while j < m and T[k] == P[j]:
            j += 1
            k += 1

        if j == m: r.append(i)

    return r


if __name__ == "__main__":
    if len(argv) > 2:

        p = argv[1]
        t = open(argv[2]).read()

        print(forca_bruta(p,t))