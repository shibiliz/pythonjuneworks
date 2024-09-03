
text="pneumonoultramicroscopicsilicovolcanoconiosis"


vowel="aeiou"

v_count=0

for ch in text:

    if vowel.count(ch)!=0:

        v_count+=1

print(v_count)

# print consunt count

text="ahello"

vowel="aeiou"

v_count=0

for ch in vowel:
     v_count+=text.count(ch)
print(v_count)



