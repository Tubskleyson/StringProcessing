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

    M = {}



    for c in P:
        M[c] = 0


    for j in range(m):
        M[P[j]] = M[P[j]] | 2**(m-j-1)




    R = [0 for _ in range(k+1)]

    for j in range(k+1):
        R[j] = (2**j -1) * 2**(m-j)

    for i in range(n):

        Ra = R[0]

        if T[i] in P: Rn =  ((Ra >> 1) | 2 **(m-1)) & M[T[i]]
        else: Rn = ((Ra >> 1) | 2 **(m-1)) & 0

        R[0] = Rn

        for j in range(1,k+1):

            if T[i] in P: Rn = ((R[j] >> 1) & M[T[i]]) | Ra | ((Ra | Rn) >> 1)

            else: Rn = ((R[j] >> 1) & 0) | Ra | ((Ra | Rn) >> 1)

            Ra= R[j]

            R[j] = Rn | 2**(m-1)

        if Rn & 1 != 0 :r.append(i)

    return r

if __name__ == "__main__":

 if len(argv) > 2:

    p = argv[1]
    t = open(argv[2]).read()

    print(shift_and_aprox(p,t))