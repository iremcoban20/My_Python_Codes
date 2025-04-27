'''
def yazdir():
    for i in range(1,11):
        print(i)
yazdir()

def my_func_1(sayi_1,sayi_2):
    for i in range(sayi_1,sayi_2+1):
        print(i)
num1=10
num2=18
my_func_1(num1,num2)

#1 den 10 a kadar olan sayıların toplamı
toplam=0
for i in range(1,11):
    print(f"sayı ={i} \t Toplam ={i}+{toplam}={i+toplam}")
    toplam=toplam+i


def toplamyazdir(sayi1,sayi2):
    toplam=0
    for i in range(sayi1,sayi2+1):
        print(f"sayi ={i} \t toplam ={i}+ {toplam} ={i+toplam}")
        toplam=toplam+i

toplamyazdir(5,15)

def my_func_2(sayi1,sayi2):
    toplam=0
    for i in range(sayi1,sayi2):
        toplam=toplam+i
    print(f"{sayi1} ve {sayi2} arasındaki sayıların tamamının toplamı ={toplam}")
my_func_2(1,11)

metin ="İrem Çoban"
print(f"büyük harfe dönmüş hali= {metin.upper()}")

def buyukyazdir(ifade:str):
    print(ifade.upper())
buyukyazdir("Ztyo Makü")

my_list=["aslan","ceylan","baykuş","karga","atmaca","civciv"]
print(f"listenin ilk hali = {my_list}")
for harf in my_list[:]:
    if harf[0] == 'a' or harf[0] =='c':
        my_list.remove(harf)
  
print(f"Listenin son hali = {my_list}")
'''
#GERİYE DEĞER DÖNDÜREN FONKSİYONLAR
def toplam(a,b):
    return a+b
print(toplam(5,3))
sonuc=toplam(9,1)
print(sonuc)         