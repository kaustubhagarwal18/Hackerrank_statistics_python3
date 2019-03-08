# Enter your code here. Read input from STDIN. Print output to STDOUT

from statistics import median
n=int(input())     # take integer input from user
arr=[int(x) for x in input().split()]    # store the numbers in a array
arr.sort()   # sort the array
   
t=int(len(arr)/2)   # find out how many elements are there
if len(arr)%2==0:   # if even integers
    L=arr[:t]
    U=arr[t:]
else:              # if odd integers
    L=arr[:t]
    U=arr[t+1:]
    
print(int(median(L)))
print(int(median(arr)))
print(int(median(U)))
