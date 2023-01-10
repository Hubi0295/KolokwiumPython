from random import random

m = int(input("m = "))
arr = []
for i in range(m):
    elem = round(random(),2)
    arr.append(elem)
arr.sort()
bucket = []
bucket_num = 10
for i in range(bucket_num):
    bucket.append([])
t=0.1
robocza=[]
i=0
licznik=0
while t<1:
    while i<len(arr) and arr[i]<t:
        robocza.append(arr[i])
        i += 1
    bucket[licznik]=robocza
    licznik+=1
    robocza=[]
    t += 0.1
print(arr)
print(bucket)