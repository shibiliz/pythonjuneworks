expence=[12000,13000,14000,15000,21000,230000,70000]

expence_count=len(expence)



for i in range(0,(expence_count)):



    if expence[i]>15000:



        print(expence[i])

# print total expence

total_expence=0

for i in range(0,len(expence)):

    total_expence=total_expence+expence[i]

print(total_expence)

# avarage 

avarage_expence=total_expence//len(expence)

print(avarage_expence)

    