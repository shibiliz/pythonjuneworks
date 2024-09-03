from re import fullmatch

variable_name=input("enter a variable name")

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,variable_name)

print ("invalid" if matcher==None else "valid")

