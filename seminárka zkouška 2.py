# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 15:03:45 2014

@author: Tom
"""
import urllib
import Tkinter as tki
import datetime
import json


def cena(i):
    return i[2]


def cislo(i):
    return i[1]


def datum(i):
    return i[0]


def datum_cislo_cena(f):
    return f["date"], f["destination_number"], f["price"]


def prihl():         # klasické přihlášení
    x = jmeno.get()
    y = heslo.get()
    aut = urllib.urlencode({"user": x, "password": y})
    f = urllib.urlopen("https://www.odorik.cz/api/v1/balance?"+aut+"")
    hh = f.read()
    kred.configure(text=hh+"Kč")
    """
    dnes=datetime.datetime.now()
    mesic="%d" % dnes.month
    mesic=int(mesic)
    if mesic==1:
        prmesic=12
    else:
        prmesic=mesic-1
    dnes=str(dnes)
    do=dnes[:10]+"T"+dnes[11:19]+"Z"
    od=do[:5]+str(prmesic)+do[8:]
    vv="https://www.odorik.cz/api/v1/calls.xml?"+"user="+x+"&password="+y+"&from="+od+"&to="+do+"&direction=out"
    c=urllib.urlopen(vv)
    f=c.read()
    soubor=open("hovory.txt","w")
    soubor.write(f)
    soubor.close()
    soubor=open('hovory.txt','r')
    radky=0
    for radek in soubor:
        radky=radky+1
    soubor.close()
    poceth=radky-3                      #vyčlenění pěti posledních hovorů
    hovory=poceth/16
    odecist=hovory-5
    odec=(odecist*16)+2                 #začátek prvního chtěného hovoru

    datpat=odec+4                       #výpočet řádků datumu...
    datctv=odec+20
    dattre=odec+36
    datdru=odec+52
    datprv=odec+68
    cispat=odec+7                       #výpočet řádků čísla...
    cisctv=odec+23
    cistre=odec+39
    cisdru=odec+55
    cisprv=odec+71
    cenpat=odec+12                             #výpočet řádků ceny..
    cenctv=odec+28
    centre=odec+44
    cendru=odec+60
    cenprv=odec+76
    soubor=open("hovory.txt","r")
    radky=0
    for radek in soubor:                        #vyfiltrování chtěných řádků
        radky=radky+1

        if radky==cisprv:
            cp=radek
            delka_cisla=(len(cp)-46)
            if delka_cisla<10:
                pomocna=24+delka_cisla
                cislo=cp[24:pomocna]
                cp=cislo
            else:
                pomocna=delka_cisla-9
                pomocna1=pomocna-3
                pomocna2=24+pomocna
                pomocna3=24+delka_cisla
                pomocna4=24+pomocna1
                cislo=cp[pomocna2:pomocna3]
                predvolba="+"+cp[pomocna4:pomocna2]
                cp=predvolba+"\t"+cislo
        elif radky==cenprv:
            u=len(x)-27
            m=11
            n=11+u
            cep=radek[m:n]+"Kč"
        elif radky==cisdru:
            cd=radek
            delka_cisla=(len(cd)-46)
            if delka_cisla<10:
                pomocna=24+delka_cisla
                cislo=cd[24:pomocna]
                cd=cislo
            else:
                pomocna=delka_cisla-9
                pomocna1=pomocna-3
                pomocna2=24+pomocna
                pomocna3=24+delka_cisla
                pomocna4=24+pomocna1    
                cislo=cd[pomocna2:pomocna3]
                predvolba="+"+cd[pomocna4:pomocna2]
                cd=predvolba+"\t"+cislo
        elif radky==cendru:
            u=len(x)-27
            m=11
            n=11+u      
            ced=radek[m:n]+"Kč"
        elif radky==cistre:
            ct=radek
            delka_cisla=(len(ct)-46)
            if delka_cisla<10:
                pomocna=24+delka_cisla
                cislo=ct[24:pomocna]
                ct=cislo
            else:
                pomocna=delka_cisla-9
                pomocna1=pomocna-3
                pomocna2=24+pomocna
                pomocna3=24+delka_cisla
                pomocna4=24+pomocna1    
                cislo=ct[pomocna2:pomocna3]
                predvolba="+"+ct[pomocna4:pomocna2]
                ct=predvolba+"\t"+cislo
        elif radky==centre:
            u=len(x)-27
            m=11
            n=11+u
            cet=radek[m:n]+"Kč"
        elif radky==cisctv:
            cc=radek
            delka_cisla=(len(cc)-46)
            if delka_cisla<10:
                pomocna=24+delka_cisla
                cislo=cc[24:pomocna]
                cc=cislo
            else:
                pomocna=delka_cisla-9
                pomocna1=pomocna-3
                pomocna2=24+pomocna
                pomocna3=24+delka_cisla
                pomocna4=24+pomocna1    
                cislo=cc[pomocna2:pomocna3]
                predvolba="+"+cc[pomocna4:pomocna2]
                cc=predvolba+"\t"+cislo
        elif radky==cenctv:
            u=len(x)-27
            m=11
            n=11+u
            cec=radek[m:n]+"Kč"
        elif radky==cispat:
            cpa=radek
            delka_cisla=(len(cpa)-46)
            if delka_cisla<10:
                pomocna=24+delka_cisla
                cislo=cpa[24:pomocna]
                cpa=cislo
            else:
                pomocna=delka_cisla-9
                pomocna1=pomocna-3
                pomocna2=24+pomocna
                pomocna3=24+delka_cisla
                pomocna4=24+pomocna1    
                cislo=cpa[pomocna2:pomocna3]
                predvolba="+"+cpa[pomocna4:pomocna2]
                cpa=predvolba+"\t"+cislo
        elif radky==cenpat:
            u=len(x)-27
            m=11
            n=11+u
            cepa=radek[m:n]+"Kč"
        elif radky==datprv:
            da1=radek[10:20]
            den=da1[8:]
            mesic=da1[5:7]
            rok=da1[:4]
            dat1=den+". "+mesic+".  "+rok
        elif radky==datdru:
            da2=radek[10:20]
            den=da2[8:]
            mesic=da2[5:7]
            rok=da2[:4]
            dat2=den+". "+mesic+".  "+rok
            
        elif radky==dattre:
            da3=radek[10:20]
            den=da3[8:]
            mesic=da3[5:7]
            rok=da3[:4]
            dat3=den+". "+mesic+".  "+rok            
            
        elif radky==datctv:
            da4=radek[10:20]
            den=da4[8:]
            mesic=da4[5:7]
            rok=da4[:4]
            dat4=den+". "+mesic+".  "+rok           
            
        elif radky==datpat:
            da5=radek[10:20]
            den=da5[8:]
            mesic=da5[5:7]
            rok=da5[:4]
            dat5=den+". "+mesic+".  "+rok          
            
    hov1=tki.Label(hl_okno, text=dat1)                               #první sloupec tabulky hovorů
    hov1.grid(row=2, column=1, padx=15, pady=3)

    hov2=tki.Label(hl_okno, text=dat2)
    hov2.grid(row=3, column=1, padx=15, pady=3)

    hov3=tki.Label(hl_okno, text=dat3)
    hov3.grid(row=4, column=1, padx=15, pady=3)

    hov4=tki.Label(hl_okno, text=dat4)
    hov4.grid(row=5, column=1, padx=15, pady=3)

    hov5=tki.Label(hl_okno, text=dat5)
    hov5.grid(row=6, column=1, padx=15, pady=3)        
 

            
    cis1=tki.Label(hl_okno, text=cp)                                #druhý sloupec tabulky hovorů
    cis1.grid(row=2, column=2, padx=15, pady=3)

    cis2=tki.Label(hl_okno, text=cd)
    cis2.grid(row=3, column=2, padx=15, pady=3)

    cis3=tki.Label(hl_okno, text=ct)
    cis3.grid(row=4, column=2, padx=15, pady=3)

    cis4=tki.Label(hl_okno, text=cc)
    cis4.grid(row=5, column=2, padx=15, pady=3)

    cis5=tki.Label(hl_okno, text=cpa)
    cis5.grid(row=6, column=2, padx=15, pady=3)
    
    cen1=tki.Label(hl_okno, text=cep)                                #třetí sloupec tabulky hovorů
    cen1.grid(row=2,column=3, padx=15, pady=3)

    cen2=tki.Label(hl_okno, text=ced)
    cen2.grid(row=3,column=3, padx=15, pady=3)

    cen3=tki.Label(hl_okno, text=cet)
    cen3.grid(row=4,column=3, padx=15, pady=3)

    cen4=tki.Label(hl_okno, text=cec)
    cen4.grid(row=5,column=3, padx=15, pady=3)

    cen5=tki.Label(hl_okno, text=cepa)
    cen5.grid(row=6,column=3, padx=15, pady=3)    


"""
def ulprihl():     #uložit přihlášení
    x=jmeno.get()
    y=heslo.get()    
    hesl=open("heslo.txt","w")    
    jmen=open("jmeno.txt","w")
    hesl.write(y)
    jmen.write(x)
    hesl.close()    
    jmen.close()
    

def prihlul():      #přihlásit přes uložené údaje 
    jmen=open("jmeno.txt","r")   
    hesl=open("heslo.txt","r")          
    x=jmen.read() 
    y=hesl.read()
    aut=urllib.urlencode({"user": x, "password": y})
    f=urllib.urlopen("https://www.odorik.cz/api/v1/balance?"+aut+"")
    hh=f.read()
    kred.configure(text=hh+"Kč")  
    od="2014-10-05T11:15:00Z"
    do="3000-10-25T11:15:00Z"
    vv="https://www.odorik.cz/api/v1/calls.json?"+"user="+x+"&password="+y+"&from="+od+"&to="+do+"&direction=out"
    c=urllib.urlopen(vv)
    f=c.read()
    g=json.loads(f,object_hook=datum_cislo_cena)
    u = len(g)
    if u>9:
        v=u-5
    elif u==9:
        v=u-4
    elif u==8:
        v=u-3
    elif u==7:
        v=u-2
    elif u==6:
        v=u-1
    else:
        v=u
    uu=0
    cis = 0
    for i in g:        
        uu = uu+1
        
        if uu>v:
            cis = cis+1
        if cis==1:
            dat1 = str(datum(i))
            cep=str(cena(i))                
            cp=str(cislo(i))
        elif cis==2:
            dat2=str(datum(i))
            ced=str(cena(i))
            cd=str(cislo(i))
        elif cis==3:
            dat3=str(datum(i))
            cet=str(cena(i))
            ct=str(cislo(i))
        elif cis==4:
            dat4=str(datum(i))
            cec=str(cena(i))
            cc=str(cislo(i))
        else:
            dat5=str(datum(i))
            cepa=str(cena(i))
            cpa=str(cislo(i))    
                    
                
            
                                  #první sloupec tabulky hovorů
    hov1.configure(text=dat1)

    
    hov2.configure(text=dat2)

    hov3.configure(text=dat3)

    hov4.configure(text=dat4)

    hov5.configure(text=dat5)       

    
                                  #druhý sloupec tabulky hovorů
    cis1.configure(text=cp)

    cis2.configure(text=cd)

    cis3.configure(text=ct)

    cis4.configure(text=cc)

    cis5.configure(text=cpa)
    
    
                             #třetí sloupec tabulky hovorů
    cen1.configure(text=cep)

    cen2.configure(text=ced)
    
    cen3.configure(text=cet)

    cen4.configure(text=cec)

    cen5.configure(text=cepa)   

    
hl_okno=tki.Tk()
uziv=tki.Label(hl_okno, text="zadejte číslo uživatele")   #vstup pro přihlášení - jméno
uziv.grid(row=0, column=0, padx=15, pady=3)
jmeno=tki.Entry(hl_okno, state="normal")
jmeno.grid(row=1, column=0, padx=15, pady=3,)

hesl_api=tki.Label(hl_okno, text="zadejte API heslo")       #vstup pro přihlášení - API heslo
hesl_api.grid(row=2, column=0, padx=15, pady=3)
heslo=tki.Entry(hl_okno, show="*")
heslo.grid(row=3, column=0, padx=15, pady=3)

x=jmeno.get()
y=heslo.get()  
aa=tki.Button(hl_okno, text="přihlásit", command=prihl, width=25)   #tlačítko pro příhlášení
aa.grid(row=4, column=0, padx=15, pady=3)

bb=tki.Button(hl_okno, text="uložit údaje", command=ulprihl, width=25)   #tlačítko pro uložení údajů
bb.grid(row=5, column=0, padx=15, pady=3)

cc=tki.Button(hl_okno, text="přihlásit naposledy uložené údaje", command=prihlul, width=25)   #tlačítko pro přihlášení přes uložené údaje
cc.grid(row=6, column=0, padx=15, pady=3)
    
    
kredit=tki.Label(hl_okno, text="Váš kredit je:")                #kredit
kredit.grid(row=0, column=1, padx=15, pady=3)    
kred=tki.Label(hl_okno, text="")
kred.grid(row=0, column=2, padx=15, pady=3, columnspan=2)


cishov=tki.Label(hl_okno, text="Datum")           #záhlaví tabulky hovorů  
cishov.grid(row=1, column=1, padx=15, pady=3)

cisloo = tki.Label(hl_okno, text="Volané číslo:")
cisloo.grid(row=1, column=2, padx=15, pady=3)

cenaa = tki.Label(hl_okno, text="Cena hovoru")
cenaa.grid(row=1, column=3, padx=15, pady=3)

hov1=tki.Label(hl_okno, text="")                               #první sloupec tabulky hovorů
hov1.grid(row=2, column=1, padx=15, pady=3)

hov2=tki.Label(hl_okno, text="")
hov2.grid(row=3, column=1, padx=15, pady=3)

hov3=tki.Label(hl_okno, text="")
hov3.grid(row=4, column=1, padx=15, pady=3)

hov4=tki.Label(hl_okno, text="")
hov4.grid(row=5, column=1, padx=15, pady=3)

hov5=tki.Label(hl_okno, text="")
hov5.grid(row=6, column=1, padx=15, pady=3)        

    
cis1=tki.Label(hl_okno, text="")                                #druhý sloupec tabulky hovorů
cis1.grid(row=2, column=2, padx=15, pady=3)

cis2=tki.Label(hl_okno, text="")
cis2.grid(row=3, column=2, padx=15, pady=3)

cis3=tki.Label(hl_okno, text="")
cis3.grid(row=4, column=2, padx=15, pady=3)

cis4=tki.Label(hl_okno, text="")
cis4.grid(row=5, column=2, padx=15, pady=3)

cis5=tki.Label(hl_okno, text="")
cis5.grid(row=6, column=2, padx=15, pady=3)
    
    
cen1=tki.Label(hl_okno, text="")                                #třetí sloupec tabulky hovorů
cen1.grid(row=2,column=3, padx=15, pady=3)

cen2=tki.Label(hl_okno, text="")
cen2.grid(row=3,column=3, padx=15, pady=3)

cen3=tki.Label(hl_okno, text="")
cen3.grid(row=4,column=3, padx=15, pady=3)

cen4=tki.Label(hl_okno, text="")
cen4.grid(row=5,column=3, padx=15, pady=3)

cen5=tki.Label(hl_okno, text="")
cen5.grid(row=6,column=3, padx=15, pady=3)    






hl_okno.mainloop()



        
