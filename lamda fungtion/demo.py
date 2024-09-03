add=lambda n1,n2:n1+n2
print(add(20,40))


sub=lambda n1,n2:n1-n2
print(sub(50,5))



cube=lambda n:n**3
print(cube(5))



max_two=lambda n1,n2:n1 if n1>n2 else n2
print(max_two(3,8))



main_two=lambda n1,n2:n1 if n1<n2 else n2
print(main_two(76,98))



last_digit_max=lambda n1,n2:n1 if n1%10>n2%10 else n2
print(last_digit_max(127,878)) 



odd_even=lambda n:"odd" if n%2!=0 else "even"
print(odd_even(7))


