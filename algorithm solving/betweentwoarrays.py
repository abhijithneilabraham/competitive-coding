import math

# function to calculate LCM
def lcmarr(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm

def gcdarr(arr):
    b=arr[0]
    for j in range(1,len(arr)):
        s=math.gcd(b,arr[j])
        b=s
    return b

def getTotalX(a, b):
    lcma=lcmarr((a))
    gcdb=gcdarr(b)
    res=[]
    for i in range(lcma,gcdb+1,lcma):
        if gcdb%i==0:
            res.append(i)
    return res
    