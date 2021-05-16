

""" 

*
*
*
*
*
*
*
*
*
* * * * * * * *


"""

def patternL(n):
	for row in range(0,n):
		print("*")
		for column in range(0,n):
			if row==n-1:
				print(" * ",end="")
			else:
				print(" ",end="")
		print()

n = 10 
patternL(n)




