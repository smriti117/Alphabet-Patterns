

""" 

* * * * * * *  
	  *
	  *
	  *
	  *
	  *
	  *
	  *
* * * * * * *


""" 

def patternI(n):
	for row in range(0,n):
		for column in range(0,n):
			if (row==0 or row==n-1 or column==n//2):
				print("*",end="")
			else:
				print(" ",end="")
		print()
n = int(input("Enter number of stars  :"))
patternI(n)