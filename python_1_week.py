'''
tam_sayi=16
ondalikli_sayi=1.6
matinsel_ifade="Irem"
metinsel_ifade_2="Coban"
mantıksal_ifade=True


tam_sayi=16
ondalıklı_sayi=1,6
matinsel_ifade="Irem"
metinsel_ifade_2="Coban"
mantıksal_ifade=True

print(f"int tipindeki değer ataması = {tam_sayi}")
print(f"float tipindeki değer ataması = {ondalıklı_sayi}")
print(f"str tipindeki değer ataması={matinsel_ifade}")
print(f"str tipindeki diğer değer ataması={metinsel_ifade_2}")



sayi_1=int(input("Lütfen birinci sayıyı giriniz = "))
sayi_2=int(input("Lütfen ikinci sayıyı giriniz ="))

print(f"Girilen iki sayının toplama işlemi = {sayi_1 + sayi_2}")
print(f"Girilen iki sayının çıkarma işlemi = {sayi_1 - sayi_2}")
print(f"Girilen iki sayının çarpma işlemi = {sayi_1 * sayi_2}")
print(f"Girilen iki sayının bölme işlemi (float) = {sayi_1 / sayi_2}")
print(f"Girilen iki sayının bölme işlemi (int) = {sayi_1 // sayi_2}") #bölme işleminde kalanın tam sayı halini verir
print(f"1. sayının karesi = {sayi_1 **2}" )
print(f"2. sayının karesi = {sayi_2 **2}")
print(f"{sayi_1}'in 6 ile bölümünden kalan = {sayi_1%6}")
print(f"{sayi_2}'nin 6 ile bölümünden kalan = {sayi_2%6}")

print(f"tamsayı değişkeni = {type(tam_sayi)}")
print(f"ondalıklı sayı değişkeni = {type(ondalikli_sayi)}")
print(f"metinsel ifade değişkeni = {type(matinsel_ifade)}")


#int tipindeki iki değeri bool tipindeki iki değere dönüştürme
mantıksal_1= True
mantıksal_2= False
new_true=bool(1)
new_false= bool(0)
print(f"int 1 değeri için bool değer karşılığı = {new_true}")
print(f"int 0 değeri için bool değer karşılığı = {new_false}")


# her bir veri için tür dönüşümü
print(f"int-> str str(15)= {str(15)}")
print(f"int ->float float(155)={float(155)}")
print(f"int-> bool str(1)= {bool(1)}")
 
print("-"*50) 

print(f"float -> int int(41.85)= {int(41.85)}")
print(f"float ->bool str(0.0)= {bool(int(0.0))}")
print(f"float -> str str(20.45)= {str(20.45)}")

print("-"*50) 

print(f"str -> int int(15)= {int(15)} ")
print(f"str-> float str(45.78) = {str(45.78)}")
print(f"str-> bool bool(int('1'))={bool(int(1))}")

print("-"*50) 

print(f"bool->int int(True) ={int(True)}")
print(f"bool->float float(int(True))) = {float(int(1.0))}")
print(f"bool-> str str(False)= {str(False)}")

new_sayi_1 = input("Lütfen bir sayı giriniz: ")
if new_sayi_1.isdigit():
    new_sayi_2 = int(new_sayi_1)
    print(f"{new_sayi_1} sayısı int'e dönüştürüldü") 

metinsel_ifade="Burdur Mehmet Akif Ersoy Üniversitesi ZTYO YBS"
print(f"{metinsel_ifade} 'nin metinsel uzunlugu {len(metinsel_ifade)} karakter uzunlugu kadardır")
print("str özel karakterler = \n ile yeni bir satıra geçeriz(new line)")
print("str özel karakterle = \t ile bir tab boşluk bırakabiliriz(t harfi)")
print(f"metinsel_ifade.count('i') ifadesi ile metinde kaç tane i karakteri olduğunu buluruz ={metinsel_ifade.count('i')}")
print(f"metinsel_ifade.find('r') ifadesi r harfinin indeks numarasını getirir(sadece str ie kullanılır) = {metinsel_ifade.find('r')}")
print(f"metinsel_ifade.index('r')ifadesi r harfinin indexini getirir ={metinsel_ifade.index('r')}")



print(f"str ile yalnızca iki işlem yapılır")
print(f"bunlardan 1. si toplamadır (+) ifadesi ile yapılır")
print(f"bu işlemin çıktısı iki kelimenin birleşik yazılmasıdır")
isim , soyisim ="Irem","Coban"
print(f"Örneğin = {isim+soyisim} gibi")
print(f"ikinci işlem ise çarpma.Python da çarpma (*)ifadesi ile str değişkenini çarparsınız")
print(f"Bu işlem size str değişkeninin çarpılan sayı kadar yanyana yazılmasına yarar")
print(f"örneğin Irem*50 işleminin sonucu 50 kere iremi yanyana yazdırmaktır= {isim*50}")
''' 
metinsel_ifade="Burdur Mehmet Akif Ersoy Üniversitesi ZTYO YBS"     
print(f"cümlenin ilk 5 harfi= {metinsel_ifade[0:5]}")
print(f"cümlenin ilk 5 harfi={metinsel_ifade[:5]}")
print(f"artış miktarının eklenmesi halinde ={metinsel_ifade[0:5:2]}")
print(f"metinsel ifadenin tersten yazılımı={metinsel_ifade[::-1]}")
print(f"metnin son indeksini getirir={metinsel_ifade[-1]}")