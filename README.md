# Proxy-Check

UNIX ve Windows uyumlu, hafif bir proxy çekme ve test etme aracı.

---

## Özellikler
- Proxyleri ProxyScrape API  üzerinden çekme.
- Dosyadan veya elle yapıştırma ile proxy listesi yükleyip çoklu iş parçacığı (thread) ile test etme.
- Sağlam (çalışan) proxyleri `proxies.txt` dosyasına kaydetme.

---

## Kurulum
1. Python 3 ve pip kurulu olmalı (Termux üzerinde `apt install python` ile sağlanır).
2. Gerekli Python paketlerini yükleyin:

```bash
pip install -r requirements.txt
```

3. (Opsiyonel) Selenium tabanlı kontrol kullanacaksanız, uygun WebDriver (Chromedriver) ve tarayıcıyı kurun.

---

## Nasıl Çalıştırılır
```bash
python main.py
```

Ardından ekrandaki menüden seçim yapın:

1) Proxy çek (Files/getproxy.py kullanır)
2) Proxy dosyasını yükle ve test et
3) Proxyleri web üzerinde kontrol et (Selenium gerekebilir)
4) Kayıtlı proxyleri göster
5) Çıkış

---

## main.py - Ön izleme (terminal "screenshot")
Aşağıda `main.py` çalıştırıldığında Termux üzerinde görebileceğiniz örnek terminal çıktısı (ASCII ön izleme) bulunmaktadır. Bunu gerçek bir ekran görüntüsü yerine README içinde hızlıca gösterim amaçlı koydum — isterseniz gerçek bir PNG ekran görüntüsünü `assets/` gibi bir klasöre koyup README'ye ekleyebiliriz.

```
  ____                 _                      _____ _          _ 
 |  _ \ ___  __ _  ___| |__   ___  _ __ ___  |  ___| |__   ___| |
 | |_) / _ \/ _` |/ __| '_ \ / _ \| '__/ _ \ | |_  | '_ \ / _ \ |
 |  __/  __/ (_| | (__| | | | (_) | | |  __/ |  _| | | | |  __/ |
 |_|   \___|\__,_|\___|_| |_|\___/|_|  \___| |_|   |_| |_|\___|_|

 Termux uyumlu Proxy-Tool - Hızlı proxy çekme ve test etme

1) Proxy çek (ProxyScrape API)
2) Proxy dosyasını yükle ve test et
3) Proxyleri web üzerinde kontrol et (Selenium gerekebilir)
4) Kayıtlı proxyleri göster
5) Çıkış

Seçiminiz: 2

Proxies dosyası bulunamadı: src/Proxy-Check/proxies.txt
Proxy dosya yolu girin (ör: /sdcard/proxies.txt) veya proxyleri satır satır yapıştırın: 
(Proxyleri yapıştırın, bitirmek için boş satır girin)
103.21.244.195:80
172.64.144.4:80

Toplam 2 proxy bulunuyor. Test başlatılıyor...
✅ Sağlam proxy sayısı: 1
Sağlam proxyler kaydedildi: src/Proxy-Check/proxies.txt
❌ Çalışmayan proxy sayısı: 1
```

---

## Dosya Yapısı
```
src/Proxy-Check/
  main.py             # Ana araç (CLI)
  requirements.txt    # Araç için bağımlılıklar
  proxies.txt         # (Otomatik oluşturulur) sağlam proxylerin kaydı
  Files/
    getproxy.py       # Proxy çekme fonksiyonu (mevcut)
    scrapesite.py     # Selenium tabanlı proxy kontrol (opsiyonel)
```

---



