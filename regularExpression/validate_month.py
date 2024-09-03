# validate month

from re import fullmatch

enter_month=input("enter a month ")

pattern="(0[1-9]|1[0-2])"

matcher=fullmatch(pattern,enter_month)

# print("invalid" if matcher==None else "valid")












