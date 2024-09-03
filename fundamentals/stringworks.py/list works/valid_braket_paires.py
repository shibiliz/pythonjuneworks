user_input="{[]"

symbal_table={"<":">",

               "[":"]",

                "(":")",

                "{":"}"
            }

top=-1

is_valid=True

symbal_stack=[]

for symbal in user_input:

    if symbal in symbal_table:

        top+=1

        symbal_stack.append(symbal)
    else:

        if len(symbal_stack)<1:

            is_valid=False

            break

        current_symbal=symbal_stack[top]

        current_symbal_closing=symbal_table[current_symbal]

        if symbal==current_symbal_closing:

            symbal_stack.pop()

            top-=1
        else:
            is_valid=False

            break

if len(symbal_stack)!=0:

    print(False)

else:

    print(is_valid)

            


