#Bjarki Þór Jónsson
k = {}
f = open("triangle2.txt","r")
listi = f.read().split("\n")
for x in range(len(listi)):
   listi[x] = listi[x].split(" ")
def path(listi,ts,ls):
    key = str(ts)+","+str(ls)
    # Gá ef gidli er í cacheinu og skila því ef það er til
    if key in k:
        return list(k[key].keys())[0]
    # Fara í næst neðstu línunni í þríhirningnum
    if len(listi)-2 == ls:
        # Finna hæstu summ fyrir næstseinasta og seinasta lið í þrí hirningnum
        gildi = int(listi[ls][ts]) + max(int(listi[ls+1][ts+1]), int(listi[ls+1][ts]))
        # setja inn gildi fyrir cacheið.
        # summa sem key   savea leiðinna í gildum                                                    hérna savea ég leiðina í x og y gildum
        k[key] = {gildi:[listi[ls][ts]+","+str(max(int(listi[ls+1][ts+1]), int(listi[ls+1][ts]))),str(ts)+","+str(ls)+":"+str(ts+1)+","+str(ls+1)]}
        # skila summunni
        return gildi
    else:
        # kalla á fallið fyrir næstu tvö gildi
        s1 = path(listi,ts,ls+1)
        s2 = path(listi,ts+1,ls+1)
        # plúsa saman summuna frá stærri leiðinni við þessa
        gildi = int(listi[ls][ts]) + max(s1,s2)
        if s1 >s2:
            #set inn í cacheið
            k[key] = {gildi:[listi[ls][ts]+","+k[str(ts)+","+str(ls+1)][s1][0],str(ts)+","+str(ls)+":"+k[str(ts)+","+str(ls+1)][s1][1]]}
        elif s2 >= s1:
            k[key] = {gildi:[listi[ls][ts]+","+k[str(ts+1)+","+str(ls+1)][s2][0],str(ts)+","+str(ls)+":"+k[str(ts+1)+","+str(ls+1)][s2][1]]}
        return gildi



s = path(listi,0,0)
#print(s)
summa = 0
# bý til listana sem þarf
for x in k.values():
    if s == list(x.keys())[0]:
        listinn =x[s]
        listi2 = listinn[0].split(",")
        stadalisti = listinn[1].split(":")
        for x in listi2:
            summa+=int(x)
# prenta út þríhirninginn með leiðinna í rauðum lit
for x in range(len(listi)):
    t = listi2[x]
    for i in range(len(listi[x])):
        if listi[x][i] == t:
            # staðfesti x gildið með cacheinu
            xgildid = int(stadalisti[x].split(",")[0])
            if xgildid == i:
                # prenta út í lit
                print("\033[0;31;0m"+listi[x][i]+"\033[0m ", end="")
            else:
                print(str(listi[x][i]) + " ", end="")
        else:
            print(str(listi[x][i])+" ",end="")
    print("")
seinastagildi = int(stadalisti[-1].split(",")[0])
bil = ""
for x in range(seinastagildi):
    bil = bil+"   "
print(bil+"\033[1;36;0m"+str(summa)+"\033[0m")
