from json import load

f=open("C:\\Users\\Admin\\OneDrive\\Desktop\\PythonJuneWorks\\json works\\filims.json")

filims=load(f)

for fl in filims:

    print(fl.get("title"))