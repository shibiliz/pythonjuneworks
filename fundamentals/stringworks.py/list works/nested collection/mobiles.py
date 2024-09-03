

mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]   


# print all mobiles name 

all_mobile_names=[ mob.get("title")for mob in mobiles]
print(all_mobile_names)

# print all brands

all_brands=[mob.get("brand") for mob in mobiles]
print (set (all_brands))

# print samsung mobile names

all_sam=[mob.get("title") for mob in mobiles if mob.get("brand")=="samsung"]
print(all_sam)


# print all mobiles available in range of 23k to 40k

price=[mob.get("title") for mob in mobiles if mob.get("price") in range (23000,40000)]
print(price) 

# print high  price mobaile

max_price=0

for mob in mobiles:

    if mob.get("price")>max_price:

        max_price=mob.get("price")



