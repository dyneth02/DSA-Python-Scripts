numberArray=list(map(int,input('Enter nubmer array: ').split()))

def bubblesort(A):
    for i in range(0,len(A)):
        for j in range(len(A)-1,0,-1):
            if A[j]<A[j-1]:
               A[j],A[j-1]=A[j-1],A[j]


bubblesort(numberArray)               
print(numberArray)
