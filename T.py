

""" 

*****
  *
  *
  *
  *


"""

n = 5 
for row in range(0,n):
	for column in range(0,n):
		if row==0 or column==n//2:
			print("*",end="")
		else:
			print(" ",end="")
	print()


