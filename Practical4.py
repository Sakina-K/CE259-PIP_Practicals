n=int(input())     #number of elements
arr=list(map(int,input().split()))  #input list
arr=list(set(list(arr)))        
a=len(arr)      #list length
arr=sorted(arr)     #sorting list 
print(arr[a-2])