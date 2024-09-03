# read a number from user
# print fizz if num is / by 3
# print buzz if num is /by 5
# print fizzbuzz if num is / by 15
num=int(input("enter a number"))

if num%15==0:
    print(f"{num} fizzbuzz")

elif num%5==0:
    print(f"{num} buzz")

elif num%3==0:
    print(f"{num} fizz")
else:
    print("invalid")    