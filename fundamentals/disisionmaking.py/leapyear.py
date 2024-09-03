year=int(input("enter a number"))


if (year%100==0 and year%400==0 )or (year%100!=0 and year%4==0):

    print(F"leap year{year}")


else:
    print("not leap year")
