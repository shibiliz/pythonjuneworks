number=int(input("enter a number"))

isprime=True
for i in range(2,number):

    if number%i==0:

        isprime=False

        break
    
print(f"{number} is prime" if isprime==True else f"{number} not prime")