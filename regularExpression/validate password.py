# 1st chasracter upper case alphabets

# next character digit from 1-9

# next digit 0-9

# 4th place 0 our 1 space 

# next 4 character any number from 0 to 9

# last character 1-9

# validate month

from re import fullmatch

enter_password=input("enter a password ")

pattern="[A-Z][1-9][0-9][0\\s]\\d{4}[1-9]{1}"

matcher=fullmatch(pattern,enter_password)

print("invalid" if matcher==None else "valid")












