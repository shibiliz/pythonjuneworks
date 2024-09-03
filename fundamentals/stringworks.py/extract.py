email_id="shibili@gmail.com"

at_indexpos=email_id.index("@")

user_name=email_id[:at_indexpos]

print(user_name)

domain=email_id[at_indexpos:]

print(domain)