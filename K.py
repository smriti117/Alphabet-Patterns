

""" 
*			*
*		*
*	*
*  *
*	*
*		*
*			*

"""
n = 9 

for row in range(0,n):
	print("*",end="")
	for column in range(0,1):
		print((n-row)*"  ",end="")
		print("*",end="")
	print()

for row in range(0,n):
	print("*",end="")
	for column in range(0,1):
		print((row)*"  ",end="")
		print("*",end="")
	print()