# Aiming to determine the percentages of A, G, C, T in the input DNA sequence.
def dna(seq):
    total_num = len(seq)  # The length of the string is the total number of nucleotides.
    # Upper case and lower case can both be included in the string.
    a_num = seq.count('A') + seq.count('a')
    g_num = seq.count('G') + seq.count('g')
    c_num = seq.count('C') + seq.count('c')
    t_num = seq.count('T') + seq.count('t')
    # Calculate the percentages.
    a_per = a_num / total_num * 100
    g_per = g_num / total_num * 100
    c_per = c_num / total_num * 100
    t_per = t_num / total_num * 100
    # Print the percentages.
    print('The percentage of A is', a_per, '%')
    print('The percentage of G is', g_per, '%')
    print('The percentage of C is', c_per, '%')
    print('The percentage of T is', t_per, '%')
    return a_per, g_per, c_per, t_per  # Returns the percentages.
# Type 'dna', and type the sequence in the parentheses with primes at the beginning and in the end to call the function.


# For example:
dna('GTAAgCTCAGaaaaaCCTCAATACAGCTCAttctGGAAGAAAATCTATTATGAATATGTG')
"""
The output is:
The percentage of A is 40.0 %
The percentage of G is 16.666666666666664 %
The percentage of C is 16.666666666666664 %
The percentage of T is 26.666666666666668 %
"""
