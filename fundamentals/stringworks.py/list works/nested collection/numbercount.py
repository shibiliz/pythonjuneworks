lst=[10,20,10,20,50,40,30]

number_count={}

for n in lst:

    if n in number_count:

        number_count[n]+=1

    else:

        number_count[n]=1
   
print(number_count)







