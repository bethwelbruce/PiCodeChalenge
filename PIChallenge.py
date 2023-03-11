def solution(P, Q):
    # count the frequency of letters in P
    freq_p = [0] * 26
    for c in P:
        freq_p[ord(c) - ord('a')] += 1

    # count the frequency of letters in Q
    freq_q = [0] * 26
    for c in Q:
        freq_q[ord(c) - ord('a')] += 1

    # count the number of distinct letters with non-zero frequency
    num_distinct = sum(1 for i in range(26) if freq_p[i] > 0 or freq_q[i] > 0)

    return num_distinct
