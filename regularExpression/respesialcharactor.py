from re import finditer

# text="abc 75rfdg#@tGHw"

# pattern="\D" # exclude digit

# pattern="\d" # print digit

# pattern="\w" # [a-zA-Z0-9]

# pattern="\\w" # special characters and space 

# pattern="\s" # space 

# patter="\S" # exclude space

matcher=finditer(pattern,text)


for m in matcher:

    print(m.start(),"===",m.group()) 