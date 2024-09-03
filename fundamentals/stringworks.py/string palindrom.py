# create a fungtion is_palindrom(word)return true if word is a palindrom string
# else return false

def is_palindrom(word):
    reversed_str=word[::-1]

    return word==reversed_str
print(is_palindrom("madam"))

# create a fungtion reversed(word)return reversed string

def reverse(word):

    reversed_str=word[::-1]

    return reversed_str
    
    print(reversed_str("hello"))


