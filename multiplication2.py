## Multiplication Table #2

i = 10
j = 10
n = 1

print("Multiplication Tables\n")

print("Select values of Multiplication to be displayed")
i = int(input("Select multiplier ->   "))
j = int(input("Select multiplicand ->  "))
n = int(input("Select starting value ->  "))
if(n>= i and n>=j):
    print("\nError, overflow! Please select value less than the multiplier and multiplicand\n")
else:
    for a in range(n,i+1):
        print("Multiplication of",a,"\n")
        for b in range(n,j+1):
            product = a*b
            print(a,"*",b,"=",product,"\n")
            if(b==j):
                print("===========\n")
    
        
