aadad = [1,2,3,4,5,6,7,8,9]
zoj = []
fard = []
for x in aadad:
    if x % 2 == 0 :
        zoj.append(x)
    else:
        fard.append(x)

print(f"zoj = {zoj}")
print(f"fard = {fard}")