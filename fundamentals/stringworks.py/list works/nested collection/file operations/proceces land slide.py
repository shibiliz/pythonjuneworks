f_=open("C:\\Users\\Luminar\\Desktop\\PythonJuneworks\\FileOperations\\land_slides.txt","r")

data=[]

for line in f:

    lst=line.rstrip("\n").split(" ")

    dic={"state":lst[0],"year":lst[1],"death_count":int(lst[2])}

    data.append(dic)

print(data) 