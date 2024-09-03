# longest palandromic substring from given string

text="racecar"

longest_palindrom=""

for i in range(0,len(text)):

    left=i

    right=i

    while(left>=0 and right<len(text) and text[left]==text[right]):
        

        current_palindrom_text=text[left:right+1]

        if len(current_palindrom_text) > len(longest_palindrom):

            longest_palindrom=current_palindrom_text

        left=left-1

        right=right+1

print(longest_palindrom)





