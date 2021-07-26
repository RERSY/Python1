##Fibonacci using recursion

def fibo_recursion(n):
    if n<=1:
        return n
    else:
        return(fibo_recursion(n-1) + fibo_recursion(n-2))

term = int(input("Please enter value ->  "))
if term<=0:
    print("Error, please input positive value.")

else:
    print("Fibonacci sequence: \t")
    for i in range(term):
        print(fibo_recursion(i))
        
