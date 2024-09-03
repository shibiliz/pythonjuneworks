from json import load

f=open("C:\\Users\Admin\\OneDrive\\Desktop\\PythonJuneWorks\\json works\\prodect.json","r",encoding="UTF-8")

items=load(f)

# print(len(items))

prodect_title=[p.get("title")for p in items]

#  print(prodect_title)

jewelery_prodect=[i.get("title")for i in items if i.get("category")=="jewelery"]

# print(jewelery_prodect)

price_range=[i.get("title") for i in items if i.get("price") > 100]


# print(price_range)

price_range=[i.get("title")for i in items if i.get("price")>100 and i.get("price")<150]

# print(price_range)

# prodect whith most number of riting

def get_rating_count(dic):

    return dic.get("rating").get("count")

top_rating_prodect=max(items,key=get_rating_count)

print(top_rating_prodect)