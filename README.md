# 👁️ YOLOv8 Real-Time Object Detection & Recording App

Bu proje, **Python**, **PyQt5** ve **YOLOv8** kullanılarak geliştirilmiş, gerçek zamanlı nesne tanımlama ve video kayıt yeteneğine sahip bir masaüstü uygulamasıdır. Kullanıcı dostu arayüzü sayesinde belirli nesne sınıflarını (insan, bardak, sandalye vb.) seçebilir ve tespit edilen görüntüleri anlık olarak yerel sürücünüze kaydedebilirsiniz.

---

## ✨ Öne Çıkan Özellikler

* 🚀 **Gerçek Zamanlı Tespit:** Ultralytics YOLOv8 modelini kullanarak düşük gecikmeli nesne algılama.
* 🎥 **Video Kayıt Sistemi:** Algılanan kareleri otomatik olarak `.mp4` formatında yüksek kalitede kaydeder.
* 🖥️ **Modern Arayüz:** PyQt5 ile tasarlanmış, kullanımı kolay ve dinamik buton yönetimi.
* 🎯 **Sınıf Filtreleme:** ComboBox üzerinden sadece ilgilendiğiniz nesneleri (Person, Cup, Chair) izleme imkanı.
* 📂 **Otomatik Klasör Yönetimi:** Çıktı videolarını tarih ve saat damgasıyla belirlenen klasörde otomatik organize eder.

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji | Kullanım Amacı |
| :--- | :--- |
| **Python** | Ana programlama dili |
| **PyQt5** | Grafiksel Kullanıcı Arayüzü (GUI) tasarımı |
| **OpenCV** | Video işleme ve görüntü format dönüştürme |
| **YOLOv8** | Derin öğrenme tabanlı nesne tespiti |
| **QThreading** | Arayüzün donmasını engellemek için eşzamanlı video işleme |

---

## 🚀 Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### 1. Depoyu Klonlayın
```bash
git clone [https://github.com/kullaniciadi/proje-adi.git](https://github.com/kullaniciadi/proje-adi.git)
cd proje-adi
2. Gerekli Kütüphaneleri Yükleyin
Bash
pip install ultralytics PyQt5 opencv-python numpy
3. Modeli ve UI Dosyasını Hazırlayın
Model: yolov8n.pt dosyasının ana dizinde olduğundan emin olun (ilk çalıştırmada otomatik indirilir).

Arayüz: .ui dosya yolunun kod içerisindeki uic.loadUi kısmında (örneğin: C:\Users\...\nesneTanımlama.ui) kendi bilgisayarınıza göre doğru tanımlandığını kontrol edin.

4. Uygulamayı Başlatın
Bash
python main.py
📖 Kullanım Kılavuzu
Kamera Başlatma: Uygulama açıldığında "Camera Start" butonuna basarak canlı yayını başlatın.

Nesne Seçimi: Açılır menüden (ComboBox) algılanmasını istediğiniz nesne tipini (person, cup, chair vb.) seçin.

Kayıt İşlemi: * "Record Start" butonuna basarak o anki işlenmiş görüntüyü videoya kaydetmeye başlayın.

Kayıt sırasında buton ismi "Record Stop" olarak değişecektir.

Durdurma: * "Record Stop" ile mevcut video kaydını bitirebilirsiniz.

"Stop" butonu ile kamerayı tamamen kapatabilir veya uygulamadan çıkış yapabilirsiniz.

📁 Dosya Yapısı
main.py: Uygulamanın ana mantığı, buton kontrolleri ve GUI yönetimi burada yer alır.

video.py: Kamera okuma, YOLO modelini çalıştırma ve görüntü işleme süreçlerini yöneten VideoThread sınıfını içerir.

nesneTanımlama.ui: Qt Designer ile hazırlanmış, uygulamanın görsel arayüz tasarımı.

/output_videos: Kaydedilen videoların tarih-saat damgasıyla saklandığı varsayılan klasör.
