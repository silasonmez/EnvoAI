from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Başlık
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(80, 10, 111, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(34, 104, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, QtGui.QBrush(QtGui.QColor(120, 120, 120)))
        self.header.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        self.header.setFont(font)
        self.header.setObjectName("header")

        # Şehir, ilçe, mahalle seçimleri
        self.combo_il = QtWidgets.QComboBox(self.centralwidget)
        self.combo_il.setGeometry(QtCore.QRect(20, 60, 221, 28))
        self.combo_ilce = QtWidgets.QComboBox(self.centralwidget)
        self.combo_ilce.setGeometry(QtCore.QRect(20, 100, 221, 28))
        self.combo_mahalle = QtWidgets.QComboBox(self.centralwidget)
        self.combo_mahalle.setGeometry(QtCore.QRect(20, 140, 221, 28))

        # Analiz butonu
        self.pushButton_analiz = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_analiz.setGeometry(QtCore.QRect(59, 180, 181, 32))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_analiz.setFont(font)
        self.pushButton_analiz.setObjectName("pushButton_analiz")
        self.pushButton_analiz.clicked.connect(self.analizEt)

        # Arama ikonu
        self.pushButton_ara = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ara.setGeometry(QtCore.QRect(20, 180, 32, 32))
        self.pushButton_ara.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\icons/pushButton_ara.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ara.setIcon(icon)

        # Logo
        self.icon = QtWidgets.QLabel(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(20, 0, 60, 60))
        self.icon.setPixmap(QtGui.QPixmap("ui\\../../Envo AI/icons/ChatGPT Image 4 May 2025 17_56_51.png"))
        self.icon.setScaledContents(True)

        # Harita
        self.widget_harita = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget_harita.setGeometry(QtCore.QRect(260, 9, 531, 541))

        # Görsel alanlar
        self.label_visual1 = QtWidgets.QLabel(self.centralwidget)
        self.label_visual1.setGeometry(QtCore.QRect(60, 490, 60, 60))
        self.label_visual1.setPixmap(QtGui.QPixmap("ui\\../../Envo AI/icons/preview.jpg"))
        self.label_visual1.setScaledContents(True)

        self.label_visual2 = QtWidgets.QLabel(self.centralwidget)
        self.label_visual2.setGeometry(QtCore.QRect(130, 490, 60, 60))
        self.label_visual2.setPixmap(QtGui.QPixmap("ui\\../../Envo AI/icons/E-Goal-15-1024x1024.png"))
        self.label_visual2.setScaledContents(True)

        # Not alanı
        self.textBrowser_note = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_note.setGeometry(QtCore.QRect(20, 310, 221, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textBrowser_note.setFont(font)

        # Skor alanı
        self.textBrowser_skor = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_skor.setGeometry(QtCore.QRect(80, 220, 100, 80))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(34, 104, 64))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, QtGui.QBrush(QtGui.QColor(120, 120, 120)))
        self.textBrowser_skor.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        self.textBrowser_skor.setFont(font)

        # ⚠️ Uyarı başlığı
        self.label_uyari = QtWidgets.QLabel(self.centralwidget)
        self.label_uyari.setGeometry(QtCore.QRect(20, 270, 240, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_uyari.setFont(font)
        self.label_uyari.setStyleSheet("color: red;")
        self.label_uyari.setText("")

        # Menü çubuğu
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuEnvato_AI = QtWidgets.QMenu(self.menubar)
        self.menuEnvato_AI.setTitle("Envo AI")
        self.menubar.addAction(self.menuEnvato_AI.menuAction())
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Envo AI"))
        self.pushButton_analiz.setText(_translate("MainWindow", "Analiz Et"))

    def analizEt(self):
        # Örnek skor üret
        import random
        skor = random.uniform(0, 100)

        # Skoru göster
        self.textBrowser_skor.setText(f"{skor:.2f}")

        # %35 üstü kontrolü
        if skor > 35:
            self.label_uyari.setText("⚠️ Dikkat: Skor değeri yüksek riskte!")
        else:
            self.label_uyari.setText("")
