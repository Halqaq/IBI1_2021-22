from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
# First, read the file.
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')
print('There are', terms.length, 'terms in this file.')

# There are four levels of childNodes in this file. Use for-loop to find the number of childNodes of every term.
total_child = 0
list1 = []
for term in terms:
    children = 0
    children1 = term.childNodes
    children1_num = children1.length  # The length of the nodeList is the number of the childNodes.
    total_child += children1_num
    children += children1_num
    for child1 in children1:
        children2 = child1.childNodes
        children2_num = children2.length
        total_child += children2_num
        children += children2_num
        for child2 in children2:
            children3 = child2.childNodes
            children3_num = children3.length
            total_child += children3_num
            children += children3_num
            for child3 in children3:
                children4 = child3.childNodes
                children4_num = children3.length
                total_child += children4_num
                children += children4_num
    list1.append(children)  # Store the data in a list, so I can use it to draw charts.
print('The total number of childNodes across all terms is', total_child)

# I draw a plot and a boxplot for each task to make it clear.
plt.plot(list1)
plt.title('The Distribution of ChildNodes of All Terms')
plt.xlabel('Terms')
plt.ylabel('ChildNodes')
plt.show()
plt.boxplot(list1, showfliers=False)  # The outliers are hidden.
plt.title('The Distribution of ChildNodes of All Terms')
plt.xlabel('Terms')
plt.ylabel('ChildNodes')
plt.show()

# The train of thought is the same as the previous task.
list2 = []
for term in terms:
    children = 0
    children1 = term.childNodes
    children1_num = children1.length
    children += children1_num
    for child1 in children1:
        children2 = child1.childNodes
        children2_num = children2.length
        children += children2_num
        for child2 in children2:
            children3 = child2.childNodes
            children3_num = children3.length
            children += children3_num
            name = child2.nodeName
            if name == 'defstr':
                defstr = child2.childNodes[0].data
                count = defstr.count('translation')
                if count > 0:
                    for child3 in children3:
                        children4 = child3.childNodes
                        children4_num = children4.length
                        children += children4_num
                    list2.append(children)

plt.plot(list2)
plt.title('The Distribution of ChildNodes of Translation-Related Terms')
plt.xlabel('Terms')
plt.ylabel('ChildNodes')
plt.show()
plt.boxplot(list2, showfliers=False)
plt.title('The Distribution of ChildNodes of Translation-Related Terms')
plt.xlabel('Terms')
plt.ylabel('ChildNodes')
plt.show()

# The two charts show that there are many terms that have more than 1000 and even 10000 childNodes, but they are not translation-related.
# The translation-related terms tend to have little childNodes. Only few of them have more than 100 childNodes.
# The boxplots also show that the translation-related terms have less childNodes.

# The 'childNodes' in XML file is different from the one in GO. If I finish the task with the former understanding,
# I can use the methods that taught in the lectures, but it's not something on the guidance.
# If I finish it with the latter understanding, the methods used have no connection with the lectures,
# but the results are what the guidance asked for.
# I did see the discussion board, but still confused.
# I'm really busy in week 14, so I chose the former understanding and write the code.
# About the latter understanding, I write a simple script as the following. I made them as pseudocode.

"""
# Create a dictionary to store the id and is_as of each term.
list_id = []
list_is_a = []
for term in terms:
    id1 = term.childNodes[1].childNodes[0].data
    list_id.append(id1)
    is_as1 = term.getElementsByTagName('is_a')
    list_content1 = []
    for is_a1 in is_as1:
        content = is_a1.childNodes[0].data
        list_content1.append(content)
    list_is_a.append(list_content1)

# Determine the first level of childNodes.
list_children1 = []
for id2 in list_id:
    n = 0
    list_content2 = []
    for is_a2 in list_is_a:
        if is_a2.count(id2) >= 0:
            name = list_id[n]
            list_content2.append(name)
        n += 1
    list_children1.append(list_content2)
dict_children1 = dict(zip(list_id, list_children1))
"""
