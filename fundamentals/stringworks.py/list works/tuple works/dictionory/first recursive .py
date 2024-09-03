text="ABACDDB"

word_count={}

for c in text:

    if c in word_count:

        print(c,"first recursive character")

        break 
    else:

        word_count[c]=1