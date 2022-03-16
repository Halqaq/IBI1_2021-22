#Every triangle is a line more than the previous one, and the point number of the adding line is increasing.
#So we need a variable outside the for-loop and a increasing variable inside the loop.
#So that we can have both values accumulating.





a=0
for i in range(1,11):
	a+=i
	print("triangle",i,"is",a)