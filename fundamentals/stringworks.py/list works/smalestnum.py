num=[1,3,6,8,5,4,99,34]


smallest_num=num[-1]

secon_smallest=num[0]

for i in num:
    if i < secon_smallest and i < smallest_num:

        secon_smallest=smallest_num

        smallest_num=i

    elif i< secon_smallest and i> smallest_num:

        secon_smallest=i

print(secon_smallest)

        
    

    

