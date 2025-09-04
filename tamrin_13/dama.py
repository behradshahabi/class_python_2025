dama = [16 , 12 , 6 , 34 , 24 , 9 , 4 , 21]
kamtarin = []
bishtarin = []
for x in dama :
    if x < 5 :
        kamtarin.append(x)
    else :
        bishtarin.append(x)
print (f"kamtarin : {kamtarin}")
print (f"bishtarin : {bishtarin}")