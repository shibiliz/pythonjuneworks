from re import finditer

text="abcd45ghj678#ds"

# pattern="[a-z0-9]{3}"

# pattern="([c-h]|[j-z])"

# pattern="([a-z]{3}|[0-9]{3})"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"===",m.group())




