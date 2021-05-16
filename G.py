
""" 

  * * * * 
*	
*
*		* * 
* 		* *
 * * * *  *

"""

def patternG(n):
	for row in range(n):
		for column in range(n):

			if( row==0 or column==0 or row==n-1 or (row == n-2 and column==n-2)
				or (row == n-3 and column==n-2)
				or (row == n-2 and column==n-1)
				or (row == n-3 and column==n-1)
				):
				print(" * ",end="")
			else:
				print("  ",end=" ")

		print()

n = int(input("Enter number of stars  :"))
# n=5
patternG(n)

