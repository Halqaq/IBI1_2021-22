import pandas as pd
import re
df = pd.read_excel('BLOSUM.xlsx')
title = 'ARNDCQEGHILKMFPSTWYVBZX'
file1 = open('DLX5_human.fa')
file2 = open('DLX5_mouse.fa')
file3 = open('RandomSeq.fa')
content1 = file1.read()
content2 = file2.read()
content3 = file3.read()
list1 = re.findall(r'[A-Z]{10}[A-Z]+', content1)
list2 = re.findall(r'[A-Z]{10}[A-Z]+', content2)
list3 = re.findall(r'[A-Z]{10}[A-Z]+', content3)
human = list1[0]
mouse = list2[0]
random = list3[0]


def blosum(seq1, seq2):
    per = 0
    edit_distance = 0  # Set initial distance as zero.
    for i in range(len(seq1)):  # Compare each amino acid.
        line = title.find(seq1[i])
        column = title.find(seq2[i]) + 1
        score = df.values[line, column]
        edit_distance += score
        if seq1[i] == seq2[i]:
            per += 1
    print(edit_distance)
    print(per*100/len(seq1), '%')


blosum(human, mouse)
blosum(human, random)
blosum(mouse, random)
