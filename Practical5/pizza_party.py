#We have the formula p=(n**2+n+2)/2, so just need to let it stop when reaching 64 slices.
#That means using "break".

a=0
for i in range(1,20):
	a=(i**2+i+2)/2
	print("after cut",i,",there are",a,"pieces of pizza.")
	if a>64:
		break