from re import fullmatch

enter_date=input("enter a date")

pattern="(0?[1-9]|[0-9]|2[0-9]|3[0-1])"

matcher=fullmatch(pattern,enter_date)

print("invalid" if matcher==None else "valid")







