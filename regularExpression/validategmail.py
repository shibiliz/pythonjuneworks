# g mail id pattern

from re import fullmatch

g_mail=input("enter a g_mail")

pattern="[a-zA-Z0-9]+(@gmail.com)"


matcher=fullmatch(pattern,g_mail)


print("invalid" if matcher==None else ("valid"))


# + match one or more

# ? optional

# * zero or more


