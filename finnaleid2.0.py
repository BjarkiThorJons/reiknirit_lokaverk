#Bjarki Þór Jónsson
k = {}
f = open("triangle2.txt","r")
listi = f.read().split("\n")
l = {}
for x in range(len(listi)):
   listi[x] = listi[x].split(" ")
def path(listi,ts,ls):
    key = str(ts)+","+str(ls)
    if key in k:
        return list(k[key].keys())[0]
    if len(listi)-2 == ls:
        gildi = int(listi[ls][ts]) + max(int(listi[ls+1][ts+1]), int(listi[ls+1][ts]))
        k[key] = {gildi:[listi[ls][ts]+","+str(max(int(listi[ls+1][ts+1]), int(listi[ls+1][ts]))),str(ts)+","+str(ls)+":"+str(ts+1)+","+str(ls+1)]}
        return gildi
    else:
        s1 = path(listi,ts,ls+1)
        s2 = path(listi,ts+1,ls+1)
        gildi = int(listi[ls][ts]) + max(s1,s2)
        if s1 >s2:
            k[key] = {gildi:[listi[ls][ts]+","+k[str(ts)+","+str(ls+1)][s1][0],str(ts)+","+str(ls)+":"+k[str(ts)+","+str(ls+1)][s1][1]]}
        elif s2 >= s1:
            k[key] = {gildi:[listi[ls][ts]+","+k[str(ts+1)+","+str(ls+1)][s2][0],str(ts)+","+str(ls)+":"+k[str(ts+1)+","+str(ls+1)][s2][1]]}
        return gildi



s = path(listi,0,0)
#print(s)
summa = 0
for x in k.values():
    if s == list(x.keys())[0]:
        listinn =x[s]
        print(listinn)
        listi2 = listinn[0].split(",")
        stadalisti = listinn[1].split(":")
        print(stadalisti)
        for x in listi2:
            summa+=int(x)
        print(summa)
print(listinn)
for x in range(len(listi)):
    t = listi2[x]
    for i in range(len(listi[x])):
        if listi[x][i] == t:
            xgildid = int(stadalisti[x].split(",")[0])
            if xgildid == i:
                print("["+listi[x][i]+"] ",end="")
            else:
                print(str(listi[x][i]) + " ", end="")
        else:
            print(str(listi[x][i])+" ",end="")
    print("")
