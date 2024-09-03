# v alidate pancard number

# first 3 character is alphabets

# 4th place PCAFHT

# 5th place alphabets

# 4 digit

# 1 alpabet

from re import fullmatch

pan_num=input("enter a pan num")

pattern="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"

matcher=fullmatch(pattern,pan_num)

print("invalid" if matcher==None else ("valid"))
