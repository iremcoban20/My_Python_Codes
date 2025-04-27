'''
def toplam_1(x,y):
    return x+y
print(toplam_1(10,5))

def kareal(a):
    return a*a
    #a**2 üs alma fonksiyonu
print(kareal(5))

def kontrol(a):    
    if a%2==0:
        return("çift")
    return("tek")

print(kontrol(kareal(6)))
#ikinci çalıştırma örneği
#sonuc=kareal(5)
#print(kontrol(sonuc))



def ornek_list_1(param_list_1:list):
    bos_liste=[]

    for aranan in param_list_1:
        if aranan[0]=="a" or aranan[0]=="f" or aranan[0]=="z":
            bos_liste.append(aranan)
    return bos_liste  
  
my_list_1=["furkan","zehra","barış","kadir","alper","yusuf","tuba"]
print(ornek_list_1(my_list_1))

def liste_2(param_list_2:list):
    bos_list_1 =[]
    bos_list_2 =[]

    for aranan_1 in param_list_2:
        if aranan_1%2==0:
            bos_list_1.append((aranan_1**3)/2)
        else:
            bos_list_2.append(aranan_1**2)
    return bos_list_1 , bos_list_2
        
my_list_2=[10,15,30,24,21]
print(liste_2(my_list_2))

def degistir(a,b):
    print(f"ilk sayı = {a}\t ikinci sayı = {b}")
    a,b=b,a
    print(f"İlk sayı = {a}\t ikinci sayı ={b}")
    return a,b
sayi_1 , sayi_2= degistir(5,6)
print(sayi_1)
print(sayi_2)

vize_list=[45,80,56,40,28,60]
final_list=[75,56,24,89,60,30]
def vize_hesaplama(param_list_1:list,param_list_2:list):
    sonuc_listesi =[]
   
    for i in range(len(param_list_1)):
        vize_not,final_not = param_list_1[i],param_list_2[i]
        ortalama =(vize_not*0,4)+(final_not*0,6)
        if ortalama>=50:
            sonuc_listesi.append("GECTİ")
        else:
            sonuc_listesi.append("KALDI")
    return sonuc_listesi

print(vize_hesaplama(vize_list,final_list))
'''
maas_listesi=[10000,20000,30000,40000,50000,60000]
print(f"Orjinal maaslar = {maas_listesi}")
print("-"*50)
def maas_zam_hesapla(liste_maas:list):
    liste_zamli =[]

    for ucret in liste_maas:
        if ucret>0 and ucret<=22000:
            liste_zamli.append(ucret*1.6) #%60 zamlı hali
        elif ucret>22000 and ucret<60000:
            liste_zamli.append(ucret*1.4)# %40 zamli
        elif ucret>60000:
            liste_zamli.append(ucret*1.15)
        else:
            pass
    return liste_zamli
print("Zamlı Maaşlar :")
print(maas_zam_hesapla(maas_listesi))

        



 