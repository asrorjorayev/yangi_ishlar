key = input("Kalitni kiriting: ")
lugat = {"ism":"Palonchi","fam":"Palonchiyev"}
if key in lugat:
    print("Key mavjud")
else:
    lugat[key]=input("Qiymatni kiriting: ")
print(lugat)