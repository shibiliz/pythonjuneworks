num=int(input("enter a number"))

total=0

while (num!=0):
    digit=num%10
    total=total+digit**3

    num=num//10
print(total)