years=[1000,1002,1003,1004,1005,1006,1007,1008]

for i in range(0,len(years)):

    if years[i]%100==0 and years[i]%400==0 or years[i]%100!=0 and years[i]%4==0:

        print(years[i])

    