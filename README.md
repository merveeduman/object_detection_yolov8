# 👁️ YOLOv8 Real-Time Object Detection & Recording App

Bu proje, **Python**, **PyQt5** ve **YOLOv8** kullanılarak geliştirilmiş, gerçek zamanlı nesne tanımlama ve video kayıt yeteneğine sahip bir masaüstü uygulamasıdır.  
Kullanıcı dostu arayüzü sayesinde belirli nesne sınıflarını (insan, bardak, sandalye vb.) seçebilir ve tespit edilen görüntüleri anlık olarak yerel sürücünüze kaydedebilirsiniz.

---

## ✨ Özellikler

- 🚀 **Gerçek Zamanlı Nesne Tespiti**  
  YOLOv8 modeli ile düşük gecikmeli ve yüksek doğrulukta algılama.

- 🎥 **Video Kayıt Sistemi**  
  İşlenen görüntüler otomatik olarak `.mp4` formatında kaydedilir.

- 🖥️ **Modern Grafik Arayüz**  
  PyQt5 ile geliştirilmiş sade ve kullanıcı dostu tasarım.

- 🎯 **Sınıf Bazlı Filtreleme**  
  ComboBox üzerinden yalnızca seçilen nesneler (Person, Cup, Chair vb.) izlenebilir.

- 📂 **Otomatik Klasör Yönetimi**  
  Çıktı videoları tarih–saat damgasıyla klasörlenerek düzenli şekilde saklanır.

- ⚙️ **Thread Destekli İşleme**  
  QThread kullanımı sayesinde arayüz donmadan video işleme devam eder.

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji | Açıklama |
|----------|----------|
| Python | Ana programlama dili |
| PyQt5 | GUI (Grafiksel Arayüz) geliştirme |
| OpenCV | Video yakalama ve görüntü işleme |
| YOLOv8 | Derin öğrenme tabanlı nesne tespiti |
| NumPy | Görüntü veri işlemleri |
| QThread | Eşzamanlı işlem yönetimi |

---

## 🚀 Kurulum

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edin:

### 1️⃣ Repoyu Klonlayın

```bash
git clone https://github.com/kullaniciadi/proje-adi.git
cd proje-adi
```

### 2️⃣ Gerekli Kütüphaneleri Kurun

```bash
pip install ultralytics PyQt5 opencv-python numpy
```

### 3️⃣ Model ve UI Dosyasını Kontrol Edin

- `yolov8n.pt` modeli ilk çalıştırmada otomatik indirilecektir.  
- `.ui` dosya yolunun kod içinde doğru tanımlandığından emin olun:

```python
uic.loadUi("nesneTanımlama.ui", self)
```

---

## ▶️ Uygulamayı Çalıştırma

```bash
python main.py
```

---

## 📖 Kullanım Kılavuzu

1️⃣ **Camera Start** butonuna basarak kamerayı başlatın.  
2️⃣ ComboBox üzerinden algılanmasını istediğiniz nesneyi seçin.  
3️⃣ **Record Start** ile kayıt işlemini başlatın.  
4️⃣ Kayıt sırasında buton adı **Record Stop** olarak değişir.  
5️⃣ **Record Stop** ile video kaydını durdurabilirsiniz.  
6️⃣ **Stop** butonu kamerayı tamamen kapatır.

---

## 📁 Proje Yapısı

```
project/
│
├── main.py                # GUI ve uygulama kontrol mekanizması
├── video.py               # Kamera okuma ve YOLO işleme thread yapısı
├── nesneTanımlama.ui      # Qt Designer arayüz dosyası
├── output_videos/         # Kaydedilen videoların bulunduğu klasör
└── README.md
```

---

## 🎯 Proje Amacı

Bu uygulama, gerçek zamanlı görüntü işleme, derin öğrenme modeli entegrasyonu ve masaüstü arayüz geliştirme süreçlerini bir arada deneyimlemek amacıyla geliştirilmiştir.  
Bilgisayarlı görü projeleri için temel bir altyapı sunar ve farklı YOLO modelleri ile kolayca genişletilebilir.

---
