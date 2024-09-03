source_word="CHICKEN"

target_word="HEN"

word_count={}

for w in source_word:

    if w in word_count:

        word_count[w]+=1

    else:
        word_count[w]=1

is_kangaru_word=True

for w in target_word:

    if w in word_count and word_count.get(w)>0:

        word_count[w]-=1
    else:

        is_kangaru_word=False

        break

print(is_kangaru_word)

    