mablagh = int(input("lotfan mablagh ra vared konid :  "))
ozviat = input("aya ozyiate vizhe darid ?  (yes/no)")

if mablagh >  500000 and ozviat == "no" :
    print (f"ersal shoma raygan ast ")
elif ozviat == "yes" :
    print (f"ersal shomaa raygan ast")
else :
    print (f"ersal shoma $50000 hazine darad")