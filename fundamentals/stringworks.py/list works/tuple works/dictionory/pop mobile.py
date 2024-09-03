mobile={"name":"vivov19","brand":"vivo","price":13000,"is_available":True}

mobile.pop("name")

print(mobile)

# add offer:500

mobile["offer"]=500

print(mobile)

# selling price

if ("offer")in mobile:

    selling_price=mobile.get("price")-mobile.get("offer")

    print(selling_price)

else:
    selling_price=mobile.get("price")

    print(selling_price)