num=int(input("enter a number"))
total=0
original=num

digit_count=len(str(num))
while (num!=0):

    digit=num%10

    exponent=digit**digit_count

    total=total+exponent

    num=num//10

print("armstrong number" if original==total else "not a armstrong number")

