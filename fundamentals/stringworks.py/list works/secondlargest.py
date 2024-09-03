num=[3,7,55,5,4,67,]

largest_num=num[0]

second_largest_num=num[0]

for i in num:

    if i>second_largest_num and  i>largest_num:

        second_largest_num=largest_num


        largest_num=i

    elif i>second_largest_num and i<largest_num:

        second_largest_num=i

print(f"second largest number is {second_largest_num}")




# wap a find the sum of odd number

# wap find the count of odd and even number in the list
