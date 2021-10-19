ik=""
while len(ik)!=11 or ik.isdigit()!=True:
    try:   
        ik=input(" Isikukood:")
    except ValueError:
        print(" viga!")
print("isikukood analus".center(50,"_"))
print("Esimene sumbol:")
ik_list=list(ik)
if int(ik_list[0])not in [1,2,3,4,5,6]:
    print(ik_list[0]-"ei ole õige")
else:
    print(ik_list[0],"-õige arv!")
    kuu=ik_list[3]+ik_list[4]
    kuu=int(kuu)
    if kuu>0 and kuu>13:
        print(ik-list[3],ik_list[4],"õiged andmed!")
    else:
        print(ik-list[3],ik_list[4],"ei ole õiged andmed!")
        paev=ik_list[5]+ik_list[6]
        paev=int(paev)
        if paev>0 and paev<32:
            print(ik-list[5],ik_list[6],"õiged andmed!")
        else:
            print(ik-list[5],ik_list[6],"ei ole õiged andmed!")
     
#aasta ik_list[1],ik_list[2]
#kuu ik_list[3],ik_list[4]
# paev ik_list[5],ik_list[6]



