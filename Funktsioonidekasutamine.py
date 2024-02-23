#from MyModul import * #Summa as s
#b=int(input("Sisesta arv2"))
#summa_3=Summa(3,b,int(input("Kolmas arv: ")))
#summa_31=Summa(100,100)

#print(summa_3)
#print(summa_31)

A = [13, 34, 4, 46, 53, 6, 63]

summa = 0

for x in A:

  if x % 2 != 0:

    summa += x

print ( summa )
