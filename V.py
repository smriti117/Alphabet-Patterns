

"""
*        *
 *      *
  *    *
   *  *
    **

"""
n=5
for i in range(0,n):
	print(i*" ",end="")
	for j in range(0,1):
		print("*",end="")
		print((n-i-1)*"  ",end="")
		print("*",end="")
	print()


