
num1=100

num2=200
print(f"values b4 swapping num1={num1} num2={num2}")# 100,200

# logic 1



temp=num1 # temp 100
num1=num2 # num1=200
num2=temp # num2=100 



print(f"after swapping num1={num1} num2={num2}")#200 100
# ligic 2


# num1=num1+num2 # num1=100+200+300
# num2=num1-num2 # num2=300-200=100
# num1=num1-num2 # num1=300-100=200
# logic 3

num1,num2=num2,num1
print(f"after swapping num1={num1} num2={num2}")

# logic 4

#num1=num1*num2
#num2=num1/num2
#num1=num1/num2

print(f"values after swapping num1={num1} num2={num2}")

