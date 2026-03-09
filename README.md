# M/M/1 Kuyruk (Bekleme Hattı) Simülasyonu

Bu proje, Python kullanılarak geliştirilmiş olay tabanlı (event-driven) bir M/M/1 kuyruk (bekleme hattı) simülasyonudur. Sistemdeki banka müşterisi gelişleri ve gişe servis süreleri üstel (exponential) dağılıma uymaktadır.

## Özellikler

- Olay tabanlı simülasyon (Event-Driven Simulation) yapısı
- Müşteri gelişleri, kuyruğa giriş/çıkış ve servis işlemlerinin modellenmesi
- 10 farklı bağımsız simülasyon deneyi ve istatistiksel analiz (Genel Ortalama ve Standart Sapma)
- Elde edilen 1000 müşteriye ait bekleme sürelerinin **Matplotlib** kullanılarak görselleştirilmesi (Histogram)

## Kurulum ve Gereksinimler

Projenin çalışması için bilgisayarınızda Python 3 yüklü olmalıdır. Projenin bağımlılıklarını izole bir ortamda kurmak için sanal ortam (virtual environment) kullanılması önerilir.

1. Bir sanal ortam (venv) oluşturun:
    ```bash
    python -m venv .venv
    ```

2. Sanal ortamı aktifleştirin:
    - **Windows için:**
        ```bash
        .venv\Scripts\activate
        ```
    - **macOS/Linux için:**
        ```bash
        source .venv/bin/activate
        ```

3. Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

*(Kullanılan başlıca kütüphaneler: `numpy` ve `matplotlib`)*

## Kullanım

Sanal ortamınız aktif durumdayken simülasyonu başlatmak için şu komutu çalıştırın:

```bash
python simulasyon.py
```

Uygulama arka planda simülasyonları çalıştıracak, sonuçları uçbirime basacak ve en sonunda verilerin görselleştirildiği bir grafik penceresi açacaktır.
