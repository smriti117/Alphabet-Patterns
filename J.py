""" 
* * * * * * * * * 
		*
		*
		*
		*
		*
*		*
  *	    * 
	*  *

"""


def patternJ(n):
	for row in range(0,n):
		for column in range(0,n):
			if(row==0 or column==n//2 
				or (row==n-1 and column==n//4)  
				or (row==n-2 and column==n//4)
				or (row==n-3 and column==n//4)):
				print("*",end="") 
			else:
				print(" ",end="")
		print()

n = 8
patternJ(n)
