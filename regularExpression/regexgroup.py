from re import finditer

text="abc123 #@KlAmd9ef"

# pattern="[ab@]" 

# pattern="[a-m]"

# pattern="[a-z]"

# pattern="[A-Z]"

# pattern="[A-Za-z]"

# pattern="[0-9]"

# pattern="[a-zA-Z0-9]"

# pattern="[^a-zA-Z0-9]"

# pattern="[\s]"

# pattern="[^a-zA-Z0-9\s]"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"===",m.group())

