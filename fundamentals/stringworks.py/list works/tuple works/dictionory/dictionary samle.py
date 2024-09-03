# dictionary>>>>>>

# dict={key:value}
# key should unique

student={"name":"sukumar","cours":"python fullstack"}
# print(student["name"])


# print(students.keys())

student["name"]="hari"
# print(student)


student["place"]="theyyotuchira" # over writes  the value if the key is presents else add as a new pair 
# print(student)

new=student.items() # 
# print(new)


student={"name":"sukumar","cours":"python fullstack"}
for i in student:
    print(f"{i}={student[i]}")



# update the course as full stack in student in iteration

student={"name":"sukumar","cours":"python full stack"}

for i in student:
    if i=="cours":
        student[i]="fullstack"
print(student)

# delete a key "place" if it present in the dict using itretion
     
for i in student:

    if i=="place":

        student.pop[i]

print(student)


