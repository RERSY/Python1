## Fibonacci sequence

print("FIBONACCI SEQUENCE using loop")

a = int(input("Please enter value->  "))
f = 0
s = 1

if a <= 0:
    print("Fibonacci sequence requested:  \t", f)

else:
    print(f,s,end = " ")
    for x in range(2, a):
        next = f+s
        print(next,end=" ")
        f = s
        s = next
            
