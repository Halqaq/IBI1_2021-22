"""
To find the genes that can be cut by EcoR1 one by one, regular expressions should be used, for every gene have the
same structure but different content. I use re.findall() to create a list of separated single genes, and output the
wanted genes into the new file in a for loop.
"""
import re  # Import first.
file1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')  # Open and save the file in a variable first.
content1 = file1.read()  # Read all the content into a string and save in content1.
file2 = open('cut_genes.fa', 'w')  # Create a new fa. file to store the chosen sequences.
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
        seq = ''.join(seq0)  # Use join() to turn the list into a string.
        length = str(len(seq))  # The number of all characters is the same as the seq length. Transform it from int to str.
        # Write name, length, and seq into file2.
        file2.write('>')  # Start with '>'.
        file2.write(name)
        file2.write('\t\t')  # Add space between name and length.
        file2.write(length)
        file2.write('\n')  # Begin another line for seq.
        file2.write(seq)
        file2.write('\n')  # Begin another line for next gene.
# Close two files at last.
file1.close()
file2.close()
