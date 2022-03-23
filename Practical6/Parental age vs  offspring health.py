# Pycharm reminds me that the imports should be at the top.
import matplotlib.pyplot as plt
# As the paternal age and the relative risk are given, a library should be created at first.
my_dic = {}
# "avh" is an abbreviation of "age vs health".
avh = {'30': 1.03, '35': 1.07, '40': 1.11, "45": 1.17, "50": 1.23, "55": 1.32, "60": 1.42, "65": 1.55, "70": 1.72, "75": 1.94}
# Then construct a scatter plot to make the data visualised.
x = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
y = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]
# I want the plot to be up triangles and in cyan color.
plt.scatter(x, y, marker="^", c="c")
plt.show()
# At last, print the value of "45" in the dictionary.
print("The relative risk of congenital heart disease for a 45-year-old father is", avh["45"])