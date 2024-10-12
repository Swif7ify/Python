
def manacher_algorithm(s):
    T = '#'.join(f'^{s}$')
    n = len(T)
    P = [0] * n
    C = R = 0

    for i in range(1, n - 1):
        mirror = 2 * C - i

        if R > i:
            P[i] = min(R - i, P[mirror])

        while T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        if i + P[i] > R:
            C, R = i, i + P[i]

    max_length = max(P)
    center_index = P.index(max_length)

    start = (center_index - max_length) // 2
    return max_length, s[start:start + max_length]

# Example usage
s = "ABABABABADDADASDBABDABABDASJHKJAABABA"
length, palindrome = manacher_algorithm(s)
print(f"Length of longest palindromic substring: {length}")
print(f"Longest palindromic substring: {palindrome}")
