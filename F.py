

""" 
* * * * *
*
*
*
*
* * * * * 
*
*
*
*
*
"""

def print_pattern(n):
	for row in range(n):
		#row = 0
		for column in range(n):
			#col = 0
			if ((row == 0  or row == n // 2) or column == 0):
				print("*", end="")
			else:
				print(" ", end="")
		print()

n = 5
print_pattern(n)




