"""
#sayi_1=int(input("birinci sayıyı giriniz ="))
#sayi_2=int(input("ikinci sayıyı giriniz ="))
#print(f"{sayi_1}>{sayi_2} = {sayi_1> sayi_2}")
#print(f"{sayi_1}<{sayi_2} = {sayi_1< sayi_2}")
#print(f"{sayi_1}>={sayi_2} = {sayi_1 >=sayi_2}")
#print(f"{sayi_1}<={sayi_2} = {sayi_1<= sayi_2}")
#print(f"{sayi_1}=={sayi_2} = {sayi_1== sayi_2}")
print(f"{sayi_1}!={sayi_2} = {sayi_1!= sayi_2}")

sayi_1=int(input("birinci sayıyı giriniz ="))
sayi_2=int(input("ikinci sayıyı giriniz ="))
print(f"{sayi_1}>{sayi_2} = {not(sayi_1> sayi_2)}")
print(f"{sayi_1}<{sayi_2} = {not(sayi_1< sayi_2)}")
print(f"{sayi_1}>={sayi_2} = {not(sayi_1 >=sayi_2)}")
print(f"{sayi_1}<={sayi_2} = {not(sayi_1<= sayi_2)}")
print(f"{sayi_1}=={sayi_2} = {not(sayi_1== sayi_2)}")
print(f"{sayi_1}!={sayi_2} = {not(sayi_1!= sayi_2)}")



sayi_1=int(input("birinci sayıyı giriniz ="))
sayi_2=int(input("ikinci sayıyı giriniz ="))
sayi_3=int(input("üçüncü sayıyı giriniz ="))

if sayi_1> sayi_2> sayi_3 or sayi_1> sayi_3>sayi_2: #sayi_1>sayi_2 and sayi_1>sayi_3 ile aynı mantık 5
    print(f"{sayi_1} sayısı en büyük sayıdır")

if sayi_2>sayi_1>sayi_3 or sayi_2>sayi_3>sayi_1:
    print(f"{sayi_2} sayısı en büyük sayıdır")

if sayi_3>sayi_1>sayi_2 or sayi_3>sayi_2>sayi_1:
    print(f"{sayi_3} en büyük sayıdır")
else:
    print(f"sayılar birbiri ile eşit olabilir")



for i in range(100):
    if i%2!=1:
        continue
    else:
        print(i)

for i in range(100):
    if i ==95:
        break
    else:
        print(i)

for i in range(2,89):
    print(i)

for i in range(5,101,5):
    print(i)
    
for i in range(5,109):
    if i%6==0: # i%2==0 and i%3==0
        print(i)

for i in range(30,300):  #3 ve 5 in katı olan çift sayılar
     if i%3==0 and i%5==0 and i%2==0:
      print(i)

sayac=0
for i in range(1,901):
      if i%21==0 and i%6!=0:
        sayac=sayac+1
        if sayac>12:
            break
        else:
          print(f"{sayac}. değer={i}")
          
        
        
print(f"21 ile tam bölünen ama 6 ile tam bölünmeyen {sayac-1}adet sayı bulunur")

for i in range(1,3):
    for j in range(3,5):
        print(f"i={i} j={j}için i+j={i+j}")

sayac_toplam=0
sayac_cift=0
for i in range(1,11):
    sayac_toplam+=1
    for j in range(11,21):
        carpim=i*j
        if carpim%2==0:
            sayac_cift +=1
            print(f"i={i} j ={j} için i*j={i*j}")
print(f"{sayac_toplam}adet çarpma işlemi yapıldı")
print(f"{sayac_cift}adet sonuc çift olarak bulundu")

my_list=[]
for i in range(1,1001):
    my_list.append(i)
print(my_list)

my_list=[]
my_list_cift=[]
for i in range(1,101):
    if i%2==0 and i%3==0:
        my_list.append(i)

    if i%2==0:
         
         my_list_cift.append(i)
         
print(my_list_cift)
print(my_list)

54 in my_list_cift

my_list_1=[1,2,3,4,5,6,7,8,9,11]
my_list_2=[10,20,3,4,5,6,7,80,90,100]
my_list_ortak=[]
my_list=[]
for i in my_list_1:
   if i in my_list_2:
      my_list_ortak.append(i)
for i in my_list_2 :
   if i not in my_list_1:
     my_list.append(i)
print(my_list_ortak)
print(my_list)
"""
my_list_1=[1,2,3,4,5,6,7,8,9,11]
my_list_2=[10,20,3,4,5,6,7,80,90,100]
my_list_birlesim=  []
my_list = []
for i in my_list_1:
    
    print(f"iki kümenin birleşimi={my_list_1.union(my_list_2)}")
    my_list_birlesim.append(i)
print(my_list_birlesim)
for i in my_list_2:
    print(f"iki kümenin kesişimi= {my_list_1.intersection(my_list_2)}")
    my_list.append(i)
print(my_list)


        





