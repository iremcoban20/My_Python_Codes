import pandas as pd #listeleme
import matplotlib.pyplot as plt #math işlemi
from tabulate import tabulate #tablo düzeni


df = pd.read_csv("students.csv", encoding="windows-1254",sep=";")

print("\nVeri (Tablolu):")
print(tabulate(df, headers='keys', tablefmt='github'))

ortalama = df['Not'].mean()
print(f"\nGenel ortalama Not : {ortalama :.2f}" )

gecenler = df[df['Not']>=50]
print("\n\tGecen öğrenciler :")
print(tabulate(gecenler, headers='keys', tablefmt='github'))

kalanlar =df[df['Not']<50]
print("\n\tKalan Öğrenciler:")
print(tabulate(kalanlar, headers='keys', tablefmt='github'))

en_yuksek_not=df[df['Not']==df['Not'].max()]
print("\n\tEn Yüksek Not:")
print(tabulate(en_yuksek_not, headers='keys', tablefmt='github'))

en_dusuk_not=df[df['Not'] == df['Not'].min()]
print("\n\tEn Düşük Not:")
print(tabulate(en_dusuk_not, headers='keys', tablefmt='github'))

ogrenci_ortalama =df.groupby('İsim')['Not'].mean().reset_index()
ogrenci_ortalama.columns = ['İsim', 'Ortalama Not']
print("\n\tÖğrenci Bazlı Ortalama Notlar:")
print(tabulate(ogrenci_ortalama, headers='keys', tablefmt='github'))

def harf_notu_hesaplama(puan):
    if puan>=85:
        return "AA"
    elif puan<85 and puan>70:
        return "BB"
    elif puan<70 and puan>50:
        return "CC"
    elif puan<50 and puan>30:
        return "DD"
    else :
        return "FF"
    
df["Harf Notu"] = df["Not"].apply(harf_notu_hesaplama)
print("\n\tHarf Notları Eklendi:")
print(tabulate(df[['Ders', 'Not', 'Harf Notu']],
               headers='keys',
               tablefmt='github'))

df.to_excel("ogrenci_notları_sonucları.xlsx",index=False)
print("\nSonuclar 'ogrenci_notları_sonucları.xlsx' dosyasına kaydedildi.")


plt.figure(figsize=(8,5))
plt.bar(ogrenci_ortalama["İsim"],ogrenci_ortalama["Ortalama Not"] , color = "green")
plt.title("Ogrenci Ortalama Notları")
plt.xlabel("Ogrenciler")
plt.ylabel("Ortalama Not")
plt.ylim(0, 100)
plt.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("ogrenci_ortalama_grafik.png")
plt.show()
print("\nGrafik 'ogrenci_ortalama_grafik.png' olarak kaydedildi.")
