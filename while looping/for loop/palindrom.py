number=int(input("enter a number"))


original=number

result=0


while(number!=0):

    digit=number%10

    result=result*10+digit

    number=number//10

print(result)

print(f"{original} is palandromic "if original==result else f"{original}is not a palindromic")



    


    
    
