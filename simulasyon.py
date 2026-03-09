import numpy as np
import matplotlib.pyplot as plt

MUSTERI_SAYISI = 100
ORTALAMA_GELIS_SURESI = 5  # Üstel dağılım için scale/beta parametresi
ORTALAMA_SERVIS_SURESI = 4 # Üstel dağılım için scale/beta parametresi

def tekil_simulasyon():
    zaman = 0.0
    gise_dolu_mu = False
    kuyruk = [] # Bekleyen müşterilerin geliş zamanlarını tutar
    
    # olaylar_listesi eleman yapısı: (olayın_gerceklesecegi_zaman, olay_turu, musteri_gelis_zamani)
    olaylar_listesi = [] 
    bekleme_sureleri = []
    
    # İlk müşterinin gelişini planlayarak simülasyonu başlatıyoruz
    ilk_gelis_suresi = np.random.exponential(scale=ORTALAMA_GELIS_SURESI)
    olaylar_listesi.append((ilk_gelis_suresi, "gelis", ilk_gelis_suresi))
    
    gelen_musteri_sayisi = 0
    
    # Döngü olay listesi boşalana veya tüm işlemler tamamlanana kadar döner
    while len(olaylar_listesi) > 0:
        # Olayları zamana göre sıralar ve ilk sıradaki olayı çekeriz
        olaylar_listesi.sort(key=lambda x: x[0])
        guncel_olay = olaylar_listesi.pop(0)
        
        # Olay bilgilerini ayrıştır ve saat bilgisini güncelle
        zaman, olay_turu, musteri_gelis_zamani = guncel_olay
        
        # --- Müşteri Gelişi (Arrival) ---
        if olay_turu == "gelis":
            gelen_musteri_sayisi += 1
            
            # Eğer toplam müşteri sayısına henüz ulaşmadıysak bir sonraki müşterinin gelişini planla
            if gelen_musteri_sayisi < MUSTERI_SAYISI:
                sonraki_gelis_suresi = np.random.exponential(scale=ORTALAMA_GELIS_SURESI)
                olaylar_listesi.append((zaman + sonraki_gelis_suresi, "gelis", zaman + sonraki_gelis_suresi))
            
            if not gise_dolu_mu:
                gise_dolu_mu = True
                # Gişe boş olduğu için beklemeksizin hemes servis başlangıcını tetikliyoruz
                olaylar_listesi.append((zaman, "servis_baslamasi", musteri_gelis_zamani))
            else:
                # Gişe dolu, müşteri kuyruğa eklenir
                kuyruk.append(musteri_gelis_zamani)
                
        # --- Servisin Başlaması (Service Start) ---
        elif olay_turu == "servis_baslamasi":
            # Müşterinin ne kadar beklediğini hesapla: (Şu anki zaman - Sisteme giriş yaptığı geliş zamanı)
            bekleme_suresi = zaman - musteri_gelis_zamani
            bekleme_sureleri.append(bekleme_suresi)
            
            # Servis süresini üstel dağılımla hesapla ve bitiş olayını planla
            servis_suresi = np.random.exponential(scale=ORTALAMA_SERVIS_SURESI)
            olaylar_listesi.append((zaman + servis_suresi, "bitis", musteri_gelis_zamani))
            
        # --- Servisin Bitmesi (Departure) ---
        elif olay_turu == "bitis":
            # Gelen müşteri sistemden ayrılır
            if len(kuyruk) > 0:
                # Kuyruk doluysa sıradaki müşteriyi (FIFO) al ve onun servis başlamasını planla
                siradaki_musteri_gelis = kuyruk.pop(0)
                olaylar_listesi.append((zaman, "servis_baslamasi", siradaki_musteri_gelis))
            else:
                # Kuyruk boşsa gişeyi boşa çıkar
                gise_dolu_mu = False

    # Bu turdaki ortalama bekleme süresini hesaplayarak döndür
    ortalama_bekleme = sum(bekleme_sureleri) / len(bekleme_sureleri) if bekleme_sureleri else 0
    return ortalama_bekleme, bekleme_sureleri


def ana_program():
    ortalama_bekleme_listesi = []
    tum_bekleme_sureleri = []
    
    print("--- 10 Bağımsız Simülasyon Çalıştırılıyor ---")
    
    # 10'lu Döngü 
    for i in range(10):
        ort_bekleme, bekleme_sureleri = tekil_simulasyon()
        ortalama_bekleme_listesi.append(ort_bekleme)
        tum_bekleme_sureleri.extend(bekleme_sureleri) # Analiz için tüm süreleri bir potada topluyoruz
        
        print(f"{i+1}. Simülasyon Ortalama Bekleme Süresi: {ort_bekleme:.4f} saniye")
        
    print("-" * 45)
    
    # İstatistiklerin Hesaplanması
    genel_ortalama = np.mean(ortalama_bekleme_listesi)
    standart_sapma = np.std(ortalama_bekleme_listesi)
    
    print(f"-> 10 Simülasyonun Genel Ortalaması:  {genel_ortalama:.4f}")
    print(f"-> 10 Simülasyonun Standart Sapması:  {standart_sapma:.4f}")
    
    # Görselleştirme (Histogram Çizimi)
    plt.figure(figsize=(10, 6))
    plt.hist(tum_bekleme_sureleri, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    
    # Ortalama değerin grafikte dik bir çizgi ile gösterilmesi (İsteğe bağlı güzel bir eklenti)
    plt.axvline(np.mean(tum_bekleme_sureleri), color='red', linestyle='dashed', linewidth=2, label=f'Genel Ortalama: {np.mean(tum_bekleme_sureleri):.2f}')
    
    plt.title('10 Simülasyonda Tüm Müşterilerin Bekleme Süresi Histogramı (M/M/1)')
    plt.xlabel('Bekleme Süresi (Saniye/Dakika)')
    plt.ylabel('Müşteri Sayısı (Frekans)')
    plt.legend()
    plt.grid(axis='y', alpha=0.5)
    
    # Grafiği Ekranda Göster
    plt.show()

if __name__ == "__main__":
    ana_program()
