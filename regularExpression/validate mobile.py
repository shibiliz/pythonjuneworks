# number start whith 678


from re import fullmatch

mob_num=input("enter a mob num")

pattern="(91)(-)?[6-9]\\d{9}"

matcher=fullmatch(pattern,mob_num)

print("invalid" if matcher==None else "valid")