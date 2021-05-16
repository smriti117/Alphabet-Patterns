
""" 
* 			* 
*			*
*			*
*			*
*			*
* * * *	* * *
*			*
*			*
*			*
*			*
*			*
"""
def pattern(n):
	for i in range(0,n):
		print(" * ",end="")
		print(n*" ",end="")
		print("  * ")

	print((n-1)*" * ")

	for j in range(0,n):
		print(" * ",end="")
		print(n*" ",end="")
		print("  * ")

n = 5	
pattern(n)