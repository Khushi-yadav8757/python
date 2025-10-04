'''Problem statement
Print the following pattern for the given N number of rows.

Pattern for N = 4
*
**
***
****
Note : There are no spaces between the stars (*)'''

Ans: N = int(input())
for i in range(1,N+1):
    for j in range(i):
        print("*", end="")
    print()    
