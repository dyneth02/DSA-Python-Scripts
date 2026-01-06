def sum(n):
    #check if n is 1, return 1 if it is
    if n==1:
        return 1
    #if n is not 1 call sum function again with n-1 input
    else:
        return sum(n-1)+n

while True:
    #get the n as a user input
    n=int(input("Please enter the nubmer : "))
    #check if the user input is -1 and esxit the loop if it is
    if n==-1:
        print("Loop is ended")
        break
    #call sum function and get summation of n numbers
    output=sum(n)
    #display summation
    print("Summation of n numbers is : ",output)
    
