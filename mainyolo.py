import sys
import cv2
import os
import numpy as np
from datetime import datetime
from ultralytics import YOLO
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap, QImage
from video import VideoThread
class ObjectDetectionApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(ObjectDetectionApp, self).__init__()
        uic.loadUi(r'C:\Users\merve\Desktop\qt_ui_projeler\nesneTanımlama.ui', self)

        self.label = self.findChild(QtWidgets.QLabel, 'label')
        self.comboBox = self.findChild(QtWidgets.QComboBox, 'comboBox')
        self.autoSave = self.findChild(QtWidgets.QCheckBox, 'autoSave')
        self.startButton = self.findChild(QtWidgets.QPushButton, 'startButton')
        self.stopButton = self.findChild(QtWidgets.QPushButton, 'stopButton')
        self.uyariLabel = self.findChild(QtWidgets.QLabel, 'uyariLabel')

        self.comboBox.addItems(['person', 'cup', 'chair'])

        self.model = YOLO('yolov8n.pt')

        self.thread = VideoThread(self.model, self.comboBox)
        self.thread.change_pixmap_signal.connect(self.update_image)

        self.startButton.clicked.connect(self.start_detection)
        self.stopButton.clicked.connect(self.stop_detection)

        self.stopButton.setEnabled(False)

        self.recording = False
        self.video_writer = None
        self.stop_clicked = False

        self.output_folder = r'C:\Users\merve\Desktop\output_videos'
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
            print(f"Kayıt klasörü oluşturuldu: {self.output_folder}")
        else:
            print(f"Kayıt klasörü zaten mevcut: {self.output_folder}")

    def update_image(self, qimg):
        if qimg is not None:
            self.label.setPixmap(QPixmap.fromImage(qimg))
            self.label.setScaledContents(True)

            if self.recording:
                frame_rgb = qimg.convertToFormat(QImage.Format_RGB888).bits().asstring(qimg.byteCount())
                frame_np = np.frombuffer(frame_rgb, np.uint8).reshape((qimg.height(), qimg.width(), 3))
                frame_bgr = cv2.cvtColor(frame_np, cv2.COLOR_RGB2BGR)

                if self.video_writer is not None and self.video_writer.isOpened():
                    self.video_writer.write(frame_bgr)
                else:
                    print("VideoWriter açılmadı veya kapalı")

    def start_detection(self):
        print("Algılama başlatılıyor")
        if self.thread.isRunning():
            self.thread.stop()
            self.thread.wait()

        self.thread = VideoThread(self.model, self.comboBox)
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

        self.startButton.setText("Record Start")
        self.startButton.clicked.disconnect()
        self.startButton.clicked.connect(self.start_recording)
        self.stopButton.setEnabled(True)

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.startButton.setText("Record Stop")
            self.uyariLabel.setText("Video kaydı başladı")
            self.start_recording_file()
        else:
            self.recording = False
            self.startButton.setText("Record Start")
            self.uyariLabel.setText("Video kaydı durduruldu")
            self.stop_recording()

    def start_recording_file(self):
        if self.label.pixmap() is None:
            print("Label pixmap is None!")
            return

        width = self.label.pixmap().width()
        height = self.label.pixmap().height()

        if width == 0 or height == 0:
            print("Label dimensions are zero!")
            return

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')


        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.temp_path = os.path.join(self.output_folder, f'{timestamp}.mp4')

        if self.video_writer is None or not self.video_writer.isOpened():
            try:
                self.video_writer = cv2.VideoWriter(self.temp_path, fourcc, 20.0, (width, height))
                if not self.video_writer.isOpened():
                    print(f"VideoWriter açılamadı! Dosya yolu: {self.temp_path}")
                    return
                print(f"Video kaydetme başladı: {self.temp_path}")
            except Exception as e:
                print(f"Video kaydetme hatası: {e}")
        else:
            print("VideoWriter zaten açık, devam ediliyor")

    def stop_recording(self):
        if self.video_writer is not None:
            self.video_writer.release()
            print("Video kaydetme durduruldu")
            self.video_writer = None

    def stop_detection(self):
        if not self.stop_clicked:
            if self.recording:
                print("Kayıt durduruluyor")
                self.stop_recording()
            else:
                print("Algılama durduruluyor")
                self.thread.stop()
                self.reset_buttons()
            self.stop_clicked = True
        else:
            print("Uygulama kapatılıyor")
            self.close()

    def reset_buttons(self):
        self.startButton.setText("Camera Start")
        self.startButton.clicked.disconnect()
        self.startButton.clicked.connect(self.start_detection)
        self.stopButton.setEnabled(False)
        self.recording = False
        self.video_writer = None

    def closeEvent(self, event):
        if self.recording:
            self.stop_recording()
        self.thread.stop()
        if self.video_writer is not None:
            self.video_writer.release()
        event.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ObjectDetectionApp()
    window.show()
    sys.exit(app.exec_())
