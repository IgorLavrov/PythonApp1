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
    kuu=int(ik_list[3]+ik_list[4])
    if kuu>0 and kuu<13:
        print(ik_list[3],ik_list[4],"õiged kuu!")
        paev=int(ik_list[5]+ik_list[6])
        if int(ik_list[0])==1 or int(ik_list[0])==2:
               aasta=int("18"+ik_list[1]+ik_list[2])
        elif int(ik_list[0]==3 or int(ik_list[0]))==4:
            aasta=int("19"+ik_list[1]+ik_list[2])
        elif int(ik_list[0]==5 or int(ik_list[0]))==6:
            aasta=int("20"+ik_list[1]+ik_list[2])
        if kuu in [1,3,5,7,8,10,12] and paev>0 and paev<32:
            print(ik_list[5],ik_list[6],"õiged paev!")
        elif(kuu in[4,6,9,11] and paev>0 and paev<31) or(kuu==2 and paev>0 and paev<29):
             print(ik_list[5],ik_list[6],"õiged paev!")
        elif aasta%4==0 and kuu==2 and paev>0 and paev<30:
            print(ik_list[5],ik_list[6],"õiged paev ; feb!")
        else:
            print(ik_list[5],ik_list[6],"ei ole õiged andmed!") 
    else:
        print(ik_list[3],ik_list[4],"ei ole õiged andmed!")
summa=0
for i in range (1,11) :
    if i <10:
        summa+=i*int(ik_list[i-1])
    else:
         summa+=(i-9)*int(ik_list[i-1])
print("Summa:",summa)
jaak=summa//11
if jaak==10:
    summa=0
    for i in range(3,13):
        if i<=9:
            summa+=i*int(ik_list[i-1])
        else:
            summa+=(i-9)*int(ik_list[i-1])
jaak=summa//11
print("1",jaak)
jaak=summa-jaak*11
print("2",jaak)
if jaak==int(ik_list[10]):
    print("isikukood on õige!!!")
else:
    print("isikukood on vale!!!")
  
