def PARTITION(A,p,r):
    x=A[p]
    i=p-1
    j=r
    while True:
        while True:          
            j=j-1
            if A[j] <= x:
                break
        while True:
            i=i+1 
            if A[i] >= x:
                break
        if i<j:
            A[i],A[j]=A[j],A[i]
        else:
            return j


def QUICKSORT(A,l,r):
    if l < r:
        q=PARTITION(A,l,r)
        QUICKSORT(A,l,q)
        QUICKSORT(A,q+1,r)


A=[23,43,3454,21,2,1]
QUICKSORT(A,0,len(A))
print(A)
    
