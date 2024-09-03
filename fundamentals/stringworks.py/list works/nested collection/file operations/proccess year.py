f_read=open("c:\\users\\luminar\\desktop\\pythonjuneworks\\fileoperations\\years.txt","r")

f_century=open("c:\\users\\luminar\\desktop\\pythonjuneworks\\fileoperations\\century.txt")

f_non_century=open("c:\\users\\luminar\\desktop\\pythonjuneworks\\fileoperations\\non_century.txt")

for year in f_read:

    yu=int(year.rstrip("\n"))

    if y % 100==0:

        f_century.write(str(y)+"\n")

    else:

        f_non_century.write(str(y)+"\n")

print(year) 