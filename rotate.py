# write a python program to rotate a list by k position
def rotate(arr,k)
    k=k%len(arr)
   return arr[-k: ] + arr[: -k]
arr =[1,2,3,4,5]
k=2
result=rotate(arr,k)
print(result)

------output-- [4,5,1,2,3]
