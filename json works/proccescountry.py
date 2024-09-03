from json import load

f=open("C:\\Users\\Admin\\OneDrive\\Desktop\\PythonJuneWorks\\json works\\country.json",encoding="UTF-8")

total_countries=load(f)

# # print(len(total_countries))

capital_name=[c.get("capital") for c in total_countries]

# # print(capital_name)

subregion_name=[c.get("subregion")for c in total_countries]

# # print(subregion_name)

region_name={c.get("region")for c in total_countries}

# print(region_name)

population_name={c.get("population")for c in total_countries}

# print(population_name)

high_population=[h.get("name")for h in total_countries if h.get("population")>55197]

# # print(high_population)

high_population=[h.get("name")for h in total_countries if h.get("population")>55197 and h.get("population")>65344]

# print(high_population)

same_alpha2Code=[s.get("name")for s in total_countries]

# print(same_alpha2Code)

same_languages=[s.get("name")for s in total_countries]

# # print(same_languages)

filter_region=[c.get("name")for c in total_countries if c.get("region")=="Asia"]

# # print(filter_region)

highest_area=max([c.get("name")for c in total_countries if c.get("area")])

# # print(highest_area)

filter_callingCodes=[f.get("name")for f in total_countries if f.get("region")=="Africa"]

# #  print(filter_callingCodes)

independent_country=[i.get("name")for i in total_countries if i.get("independent")==False]

# # print(independent_country)

independent_country=[i.get("name")for i in total_countries if i.get("independent")==True]

# # print(len(independent_country))

def high_population(dic):

    return dic.get("population")

most_population=max(total_countries,key=high_population)

# print(most_population.get("name"))

def get_area(dic):


    if "area" in dic:

        return dic.get("area")

    else:

        return 0

# lowest_area=min(total_countries,key=get_area)

#  print(lowest_area.get("name"))

region_summary={}

for c in total_countries:

    region_name=c.get("region")

    if region_name in region_summary:

        region_summary[region_name]+=c.get("area",0)
    else:

        region_summary[region_name]=c.get("area",0)

value_key=[(v,k) for k,v in region_summary.items()]

print(max(value_key))





















