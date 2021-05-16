
"""
	 * *
	*   *
	 * *
"""

def patternO(n):
	for row in range(0,n):
		for column in range(0,n):
			if (row==0 and column==((n//2)-1)) or \
				(row==0 and column==((n//2)+1)) or \
			    (row==1 and (column==((n//2)-2) or column==n-1))or \
			    (row==2 and (column==((n//2)-1) or column==n-2)):
				print("*",end="")
			else:
				print(" ",end="")
		print()

n = 5
patternO(n)



