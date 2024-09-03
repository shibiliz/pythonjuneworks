

sorted_sourse_word=sorted(sourse_word)
sorted_target_word=sorted(target_word)

def is_anagram(word1,word2):
    return sorted(word1)==sorted(word2)

sorted_sourse_word="lisen"
sorted_target_word="silent"

print(is_anagram(sorted_sourse_word,sorted_target_word))



