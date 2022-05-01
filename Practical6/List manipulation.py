# Import at first.
import matplotlib.pyplot as plt
# Input the given data.
marks = [45, 36, 86, 57, 53, 92, 65, 45]
# Print the sorted data but let the origin list stays the same.
print(sorted(marks))
# The ylabel is "marks", and the marks belong to Rob.
plt.boxplot(marks, labels=['Rob'])
plt.ylabel('marks')
plt.show()
# Calculate the average of the scores.
avg = sum(marks)/len(marks)
if avg>60:  # 60 is the passing score
    print("Rob has passed IBI1.")
else:
    print("Rob has failed in IBI1.")