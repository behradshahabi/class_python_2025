names = input("lotfan name khod ra vared konid :  ")
with open ("names.txt" , "w") as f :
    for name in names.split(","):
        f.write(f"{name.strip()}\n")

with open ("names.txt", "r") as f:
    my_names = f.readlines()
for my_name in my_names :
    print (f"hello {my_name.strip("\n")} My dear friend")
    print ("--" *18)