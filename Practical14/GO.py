from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
from copy import deepcopy
import numpy as np
# Read the file first.
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')  # Store all terms in this variable.
print('There are', terms.length, 'terms in this file.')

# In this file, we can find the parentNodes from each term. It's not easy to count the childNodes of each term.
# So I changed the direction, created a dictionary and store the terms as keys and their first-level childNodes as values.
dict1 = {}
for term in terms:
    count1 = 0
    if term.getElementsByTagName('is_a'):
        p_num = len(term.getElementsByTagName('is_a'))  # p_num = parentNodes number
        term_id = term.getElementsByTagName('id')[0].childNodes[0].data
        while count1 < p_num:
            is_a = term.getElementsByTagName('is_a')[count1].childNodes[0].data
            if is_a not in dict1:
                dict1[is_a] = [term_id]
            else:
                dict1[is_a].append(term_id)
            count1 += 1

# Next, find the childNodes in subsequent levels. Store them in dict_all.
dict_all = deepcopy(dict1)  # Use deepcopy() instead of copy() to save memory.
turn = 0
while turn < 50:
    dict3 = deepcopy(dict_all)
    for id1 in dict_all:
        set1 = (set(dict3[id1]))  # set() can delete the repetitive elements.
        dict3[id1] = set1
    for a in dict1:
        for b in dict_all[a]:
            if b in dict1:
                dict_all[a].extend(dict1[b])
    dict4 = deepcopy(dict_all)
    for id2 in dict_all:
        set2 = (set(dict4[id2]))
        dict4[id2] = set2
    if dict3 == dict4:  # When dict_all doesn't change, all childNodes are found. The while-loop then breaks.
        break
    turn += 1

for id3 in dict_all:
    set3 = (set(dict_all[id3]))  # Also set the dict_all here.
    dict_all[id3] = set3

list_all = []  # Store the number of childNodes of each term in list_all.
for y in dict_all:
    length1 = len(dict_all[y])
    list_all.append(length1)
# Determine the terms that don't have childNodes and add 0 to list_all.
# I will draw boxplot at last, so the order doesn't matter.

count2 = 0
for t in dict_all:
    count2 += 1
for r in range(0, terms.length-count2):
    list_all.append(0)

# Abstract the text of defstr, and retrieval the string to find the translation-related terms.
list_id = []
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    defstr_all = defstr.lower()  # All elements are lower case, so that if "Translation" is at the beginning of a sentence, it can be found.
    id = term.getElementsByTagName('id')[0].childNodes[0].data
    l = defstr_all.count('translation')
    if l >= 1:
        list_id.append(id)

# Determine the number of childNodes.
count3 = 0
list_translation = []
list_translation_count = []
for id1 in list_id:
    if id1 in dict_all:
        list_translation.append(dict_all[id1])
    else:
        count3 += 1
for j in range(0,count3):
    list_translation_count.append(0)
for h in list_translation:
    list_translation_count.append(len(h))

# Draw boxplot at last.
plt.boxplot(list_all, showmeans=True, showfliers=True)
plt.xlabel('Distribution of childNodes of all terms')
plt.ylabel('ChildNodes')
plt.show()
plt.boxplot(list_translation_count, showmeans=True, showfliers=True)
plt.xlabel('Distribution of childNodes of the translation-related terms')
plt.ylabel('ChildNodes')
plt.show()
print('The mean of childNodes of all terms is', np.mean(list_all))
print('The mean of childNodes of translation-related terms is', np.mean(list_translation_count))

# According to the boxplot, the means are similar. However, the translation-related terms tend to have less childNodes.
# There are translation-related terms that have hundreds of childNodes.
# There are terms that don't relate to translation have much more childNodes, the biggest number is almost 30000.
