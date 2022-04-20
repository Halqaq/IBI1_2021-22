"""
The user type the filename with the reminder. And the file would be analyzed.
The wanted sequences would be stored in 'genes_fragments'.
"""
import re
fname = input('Enter the file name: ')  # Let the user input the filename.
file1 = open(fname)  # Open the input file.
content1 = file1.read()  # Read all the content into a string and save in content1.
file2 = open('genes_fragments.fa', 'w')  # Create a new file 'gene_fragments.fa' to store the chosen sequences.
genes = re.findall(r'>.*?[AGCT\n]+\n', content1)  # Use re.findall() to separate each gene, it returns a list.
"""
Before the for loop, create a variable that stores the cut sequence which would be identified in the loop.
The cut sequence GAATTC can be in different lines, so \n can be in each interval of this sequence. 
There are 5 possibilities.
"""
cut = r'GAATTC|G\nAATTC|GA\nATTC|GAA\nTTC|GAAT\nTC|GAATT\nC'
# Variable gene stores a single gene in each cycle.
for gene in genes:
    if re.search(cut, gene):  # If cut is not identified, re.search() would return none, so use if re.search() directly.
        name0 = re.findall(r'>.*? gene:(\w+)', gene)  # Use re.findall() to get gene name after 'gene:'.
        name = name0[0]  # re.findall() returns a list with one element. Transform it into a string for further operation.
        """
        Get sequence of the gene. The method is the same. But there should be enough repetition of [AGCT].
        Because there may be similar words in basic information of the gene in the first line.
        """
        seq0 = re.findall(r'[AGCT]{5}[AGCT]+', gene)  # Exclude '\n' to make the seq in one line.
        seq = ''.join(seq0)  # Use join to turn the list into a string.
        cuts = re.findall('GAATTC', seq)  # The number of cuts in seq.
        fragments = str(len(cuts) + 1)  # The number of fragments is cuts+1. Turn it into a string.
        # Write name, fragments, and seq into file2.
        file2.write('>')  # Start with '>'.
        file2.write(name)
        file2.write('\t\t')  # Add space between name and fragments.
        file2.write(fragments)
        file2.write('\n')  # Begin another line for seq.
        file2.write(seq)
        file2.write('\n')  # Begin another line for next gene.
# Close two files at last.
file1.close()
file2.close()
