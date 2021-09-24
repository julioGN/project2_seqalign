import numpy as np

S1 = 'ACGU'
S2 = 'CGAU'
s_s1 = []
s_s2 = []
diagonal = '↖'
up = '↑'
left = '←'
stop = 'S'


def print_eddy(seq1, seq2):
    m = np.zeros((len(S1) + 1, len(S2) + 1))
    bt = [[stop for a in range(len(S1) + 1)] for b in range(len(S2) + 1)]

    i = 0
    for matching in m:
        j = 0
        for cells in matching:
            if i != 0 and j != 0:
                if S1[i-1] == S2[j-1]:
                    # m[i][j] = m[i-1][j-1] + 1
                    m[i][j] = m[i-1][j-1] + 5
                    bt[i][j] = diagonal
                if S1[i-1] != S2[j-1]:
                    m[i][j] = m[i-1][j-1] - 2
                    bt[i][j] = diagonal
                    if m[i-1][j] > m[i][j]:
                        m[i][j] = m[i-1][j] - 6
                        bt[i][j] = up
                    if m[i][j-1] > m[i][j]:
                        m[i][j] = m[i][j-1] - 6
                        bt[i][j] = left
            j += 1
        i += 1

    print("S1 = " + S1 + ", S2 = " + S2)
    print("M: ")
    print(np.matrix(m))
    max_align_score = m[i-1][j-1]
    print("Maximum alignment score: ", end='')
    print(max_align_score)
    print()
    print("Backtracking Matrix: ")
    print("BT")
    print(np.matrix(bt))

    i = len(S1)
    j = len(S2)

    while bt[i][j] != stop:
        if bt[i][j] == diagonal:
            s_s1.append(S1[i-1])
            s_s2.append(S2[j-1])
            i -= 1
            j -= 1
        if bt[i][j] == up:
            s_s1.append(S1[i-1])
            s_s2.append('-')
            i -= 1
        if bt[i][j] == left:
            s_s1.append('-')
            s_s2.append(S2[j-1])
            j -= 1

    aligned_s1 = ''
    aligned_s2 = ''
    something = 0
    while something < len(s_s1):
        aligned_s1 += s_s1.pop()
        aligned_s2 += s_s2.pop()

    print("S1: " + aligned_s1)
    print("S2: " + aligned_s2)


def main():
    print_eddy(S1, S2)


if __name__ == '__main__':
    main()