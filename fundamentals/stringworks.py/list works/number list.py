numbers=[10,11,12,56,89,76,54,34,59]

for i in range(0,len(numbers)):

    if numbers[i]%2==0:

        print(numbers[i])

# print total numbers

total=0

for i in range(0,len(numbers)):

    total=total+numbers[i]

print(total)

# odd numbers

odd_total=0

for i in range(0,len(numbers)):

    if numbers[i]%2!=0:

        odd_total=odd_total+numbers[i]

print(odd_total) 


        




    

