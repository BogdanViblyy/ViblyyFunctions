#def Summa(arv1:int,arv2:int,arv3=0)->int:
#    """ Funktsioon tagastab kolme arvu summa
#    Summa(arv1,arv2,arv3)
    
#    :param int arv1: Arv1 sisestab kasutaja
#    :param int arv2: Arv1 sisestab kasutaja
#    :param int arv3: Vaikimisi ta võrdub nulliga
#    """
#    s=arv1+arv2+arv3
#    return s


#def Clasificator(x)->any:
#    if type(x)==str:
#        s=print(x," on text")
#    if type(x)==int:
#        s=print(x," on täisarv")

#    if type(x)==str:
#        s=print(x," on float")
#    return s


#1
#def Arithmetica(arv1:float,arv2:float,operatsioon)->float:
    
#    if operatsioon=="+":
#        return arv1+arv2  
        
#    elif operatsioon=="-":
#        return arv1-arv2 
        
        
#    elif operatsioon=="*":
#        return arv1*arv2 
#    elif operatsioon=="/":
#        if not(arv2==0):
#            return  arv1/arv2 
#        else:
#            return "Nulliga jagada ei saa."
        

#    else:
#        print("Vale operatsioon")



#3

#def SquarePSD(külg:float)->any:
#    """Tagastab kolm andmeid pindala ruumala ja diagonaal
#    :param float ruudukülg sisestab kasutaja
#    Tagastab p, s, d

    
#    """
#    p=külg*4
#    s=külg**2
#    d=s*s**0.5
#    return p, s, d


##2

#def is_year_leap(aasta:int)->bool:
#    """Funktsioon otsustab kas aasta on liigassta või ei ole.
#    Tagastab True kui aasta on liigasta ja False kui aasta ei ole.
#    :param int aasta: Aasta sisestab kasutaja
#    :rtype: bool
#    """
#    if aasta%4==0 and aasta%100!=0:
#        return True
#    else:
#        return False


def season(a:int)->str:
    """
    """
    while True:
        if a>0 and a<13:
            break
        else:
           try:
               a=int(input("Ainult 1-12, Sisesta numbri veel kord: "))
           except:
               print("Vale andmetüüp")
    if a==12 or a==1 or a==2:
        s="talv"
    elif a in range(6,9,1):
        s="suvi"
    elif 9<=a<=11:
        s="sügis"
    return s