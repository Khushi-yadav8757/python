# most frequent element in a list

def mfe(arr):
  freq={}
  for num in arr:
    freq[num]=freq.get(num,0)+1
arr=[1,3,3,2,1,3,2,3]
result=mfe(arr)
print(arr)



------------------output = 3
