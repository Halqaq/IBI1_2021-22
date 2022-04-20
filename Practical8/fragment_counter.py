seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'  # Create the seq variable.
cut = seq.count('GAATTC')  # Use 'count' to count the cut number, and save it as 'cut'.
#  Total number of fragment should be 'cut+1'.
print('This sequence would be cut into', cut+1, 'pieces if we applied the EcoRI enzyme to it.')