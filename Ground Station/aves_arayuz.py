# 
# 
# GTU-AVES takımı tarafından Teknofest 2021 Uluslararası İHA Yarışması için yazılmıştır.
# YERLİ ARAYÜZ TASARIM VE YAZILIMI KAYNAK KODU
#
#
#
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import*
from dronekit import connect
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
import sys
import glob
import serial
import resources_rc

"""
Tasarlanan arayüzdeki gösterge ve logoların konum, boyut ve renk gibi özelliklerinin belirlendiği ve bu kaynakların
koda yüklendiği sınıftır. Ana pencere bu sınıf üzerinde tasarlanır. 
"""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1320, 930)
        MainWindow.setStyleSheet("background-color: rgb(136, 138, 133);")
        MainWindow.setFixedSize(1340, 930)
        MainWindow.setWindowIcon(QtGui.QIcon('aves_icon.png'))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.baslik = QtWidgets.QLabel(self.centralwidget)
        self.baslik.setGeometry(QtCore.QRect(330, -20, 541, 111))
        self.baslik.setStyleSheet("image: url(:/source/baslik.png);")
        self.baslik.setText("")
        self.baslik.setObjectName("baslik")

        self.hukLogo = QtWidgets.QLabel(self.centralwidget)
        self.hukLogo.setGeometry(QtCore.QRect(70, 790, 351, 131))
        self.hukLogo.setStyleSheet("image: url(:/source/huk_logo.png);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.hukLogo.setText("")
        self.hukLogo.setObjectName("hukLogo")

        self.avesLogo = QtWidgets.QLabel(self.centralwidget)
        self.avesLogo.setGeometry(QtCore.QRect(630, 790, 141, 111))
        self.avesLogo.setStyleSheet("image: url(:/source/aves.png);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.avesLogo.setText("")
        self.avesLogo.setObjectName("avesLogo")


        self.gtuLogo = QtWidgets.QLabel(self.centralwidget)
        self.gtuLogo.setGeometry(QtCore.QRect(980, 780, 201, 111))
        self.gtuLogo.setStyleSheet("image: url(:/source/gebze-teknik-universitesi-gtu-seeklogo.com.png);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.gtuLogo.setText("")
        self.gtuLogo.setObjectName("gtuLogo")

        self.airspeed = QtWidgets.QLabel(self.centralwidget)
        self.airspeed.setGeometry(QtCore.QRect(80, 130, 300, 300))
        self.airspeed.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.airspeed.setText("")
        self.airspeed.setPixmap(QtGui.QPixmap(":/source/airspeed.png"))
        self.airspeed.setObjectName("airspeed")

        self.arrowAirSpeed = QtWidgets.QLabel(self.centralwidget)
        self.arrowAirSpeed.setGeometry(QtCore.QRect(80, 130, 300, 300))
        self.arrowAirSpeed.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.arrowAirSpeed.setText("")
        self.arrowAirSpeed.setPixmap(QtGui.QPixmap(":/source/arrow.png"))
        self.arrowAirSpeed.setObjectName("arrowAirSpeed")
        self.arrowAirSpeed.setAlignment(QtCore.Qt.AlignCenter)

        self.altimeter = QtWidgets.QLabel(self.centralwidget)
        self.altimeter.setGeometry(QtCore.QRect(500, 130, 300, 300))
        self.altimeter.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.altimeter.setText("")
        self.altimeter.setPixmap(QtGui.QPixmap(":/source/Altimeter.png"))
        self.altimeter.setObjectName("altimeter")

        self.arrowAltimeter = QtWidgets.QLabel(self.centralwidget)
        self.arrowAltimeter.setGeometry(QtCore.QRect(500, 130, 300, 300))
        self.arrowAltimeter.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.arrowAltimeter.setText("")
        self.arrowAltimeter.setPixmap(QtGui.QPixmap(":/source/arrow.png"))
        self.arrowAltimeter.setObjectName("arrowAltimeter")
        self.arrowAltimeter.setAlignment(QtCore.Qt.AlignCenter)

        self.arrowSmall = QtWidgets.QLabel(self.centralwidget)
        self.arrowSmall.setGeometry(QtCore.QRect(500, 130, 300, 300))
        self.arrowSmall.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.arrowSmall.setText("")
        self.arrowSmall.setPixmap(QtGui.QPixmap(":/source/arrow_small.png"))
        self.arrowSmall.setObjectName("arrowSmall")
        self.arrowSmall.setAlignment(QtCore.Qt.AlignCenter)

        self.compass = QtWidgets.QLabel(self.centralwidget)
        self.compass.setGeometry(QtCore.QRect(920, 130, 300, 300))
        self.compass.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.compass.setText("")
        self.compass.setPixmap(QtGui.QPixmap(":/source/Compass.png"))
        self.compass.setObjectName("compass")
        self.compass.setAlignment(QtCore.Qt.AlignCenter)

        self.compassIndicator = QtWidgets.QLabel(self.centralwidget)
        self.compassIndicator.setGeometry(QtCore.QRect(920, 160, 301, 251))
        self.compassIndicator.setStyleSheet("image: url(:/source/aves.png);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.compassIndicator.setText("")
        self.compassIndicator.setObjectName("compassIndicator")

        self.verticalSpeed = QtWidgets.QLabel(self.centralwidget)
        self.verticalSpeed.setGeometry(QtCore.QRect(80, 470, 300, 300))
        self.verticalSpeed.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.verticalSpeed.setText("")
        self.verticalSpeed.setPixmap(QtGui.QPixmap(":/source/Vertical Speed.png"))
        self.verticalSpeed.setObjectName("verticalSpeed")

        self.arrowVerticalSpeed = QtWidgets.QLabel(self.centralwidget)
        self.arrowVerticalSpeed.setGeometry(QtCore.QRect(80, 470, 300, 300))
        self.arrowVerticalSpeed.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.arrowVerticalSpeed.setText("")
        self.arrowVerticalSpeed.setPixmap(QtGui.QPixmap(":/source/arrow.png"))
        self.arrowVerticalSpeed.setObjectName("arrowVerticalSpeed")
        self.arrowVerticalSpeed.setAlignment(QtCore.Qt.AlignCenter)

        self.attitude = QtWidgets.QLabel(self.centralwidget)
        self.attitude.setGeometry(QtCore.QRect(500, 470, 300, 300))
        self.attitude.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.attitude.setText("")
        self.attitude.setPixmap(QtGui.QPixmap(":/source/attitudeout.png"))
        self.attitude.setObjectName("attitude")

        self.turnCoord = QtWidgets.QLabel(self.centralwidget)
        self.turnCoord.setGeometry(QtCore.QRect(920, 470, 300, 300))
        self.turnCoord.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.turnCoord.setText("")
        self.turnCoord.setPixmap(QtGui.QPixmap(":/source/BankAngle.png"))
        self.turnCoord.setObjectName("turnCoord")
        
        self.turnCoordDrone = QtWidgets.QLabel(self.centralwidget)
        self.turnCoordDrone.setGeometry(QtCore.QRect(920, 470, 300, 300))
        self.turnCoordDrone.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.turnCoordDrone.setText("")
        self.turnCoordDrone.setPixmap(QtGui.QPixmap(":/source/BankAngleDrone.png"))
        self.turnCoordDrone.setObjectName("turnCoordDrone")
        self.turnCoordDrone.setAlignment(QtCore.Qt.AlignCenter)

        self.attitudeIndicator = QtWidgets.QLabel(self.centralwidget)
        self.attitudeIndicator.setGeometry(QtCore.QRect(20, -4, 1250, 1250))
        self.attitudeIndicator.setText("")
        self.attitudeIndicator.setPixmap(QtGui.QPixmap(":/source/attitude indicator.png"))
        self.attitudeIndicator.setObjectName("attitudeIndicator")
        self.attitudeIndicator.setAlignment(QtCore.Qt.AlignCenter)

        self.arm = QtWidgets.QLabel(self.centralwidget)
        self.arm.setGeometry(QtCore.QRect(10, 20, 251, 31))
        self.arm.setObjectName("arm")

        self.mode = QtWidgets.QLabel(self.centralwidget)
        self.mode.setGeometry(QtCore.QRect(10, 70, 500, 31))
        self.mode.setObjectName("mode")

        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(920, 10, 500, 31))
        self.status.setObjectName("status")

        self.blankCircle = QtWidgets.QLabel(self.centralwidget)
        self.blankCircle.setGeometry(QtCore.QRect(-1820, -1742, 5000, 5000))
        self.blankCircle.setStyleSheet("image: url(:/source/blankcircle.png);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.blankCircle.setText("")
        self.blankCircle.setObjectName("blankCircle")

        #Bu alanda kaynak dosyaların birbiri üzerine doğru bir şekilde konumlanması sağlanır
        self.attitudeIndicator.raise_()
        self.blankCircle.raise_()
        self.baslik.raise_()
        self.hukLogo.raise_()
        self.avesLogo.raise_()
        self.gtuLogo.raise_()
        self.airspeed.raise_()
        self.arrowAirSpeed.raise_()
        self.altimeter.raise_()
        self.arrowAltimeter.raise_()
        self.arrowSmall.raise_()
        self.compass.raise_()
        self.compassIndicator.raise_()
        self.turnCoord.raise_()
        self.verticalSpeed.raise_()
        self.arrowVerticalSpeed.raise_()
        self.attitude.raise_()
        self.turnCoord.raise_()
        self.turnCoordDrone.raise_()
        self.arm.raise_()
        self.mode.raise_()
        self.status.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("GTU-AVES", "GTU-AVES")) #Pencere ismi belirlenir.
"""
Araç ile veri akışı bu sınıfta yapılır. DroneKit üzerinden gelen veriler belirli bir tazeleme hızıyla yenilenir.
"""
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.data)
        timer.start(100) #Veri akış gecikmesi.
        self.data() # Veri tazeleme fonksiyonu.
    """
    Veriler bu fonksiyon içinde sürekli güncellenir. Yeni gelen veriyle değişen göstergelerin konumları 
    ve dönme miktarları bu fonksiyon içinde ayarlanır. 
    """
    def data(self):
        if avesDrone.armed == True:
            isArmed = "EVET"
        else:
            isArmed="HAYIR"
        if avesDrone._heartbeat_started == True:
            isConnected = "BAĞLANTI KURULDU"
        else:
            isConnected= "BAĞLANTI YOK"
        # Aracın arm,mod ve bağlantı durumunu gösteren etiketler burada oluşturulur. Boyut renk ve fontu ayarlanır.
        self.arm.setText(
            '<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; font-style:italic;\">ARM : {}</span></p></body></html>'.format(
                isArmed
            )
        )
        self.mode.setText(
            '<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; font-style:italic;\">MOD : {}</span></p></body></html>'.format(
                avesDrone.mode.name
            )
        )
        self.status.setText(
            '<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; font-style:italic;\">DURUM : {}</span></p></body></html>'.format(
                isConnected
            )
        )
        # Göstergeler için gerekli verilerin çekilmesi ve pencere üzerinde hareket ettirebilmek için pixmaplarinin
        # oluşturulması.
        airspeed = avesDrone.airspeed 
        altitude = avesDrone.location.global_relative_frame.alt
        comp = avesDrone.heading
        vertic = avesDrone.velocity[2]
        roll = avesDrone._roll
        pitch=avesDrone._pitch
        self.pxAirspeedArrow = QPixmap("arrow.png")
        self.pxAltitudeArrow = QPixmap("arrow.png")
        self.pxAltitudeSmallArrow = QPixmap("arrow_small.png")
        self.pxVerticalSpeedArrow = QPixmap("arrow.png")
        self.pxAttitudeIndicator = QPixmap("attitude indicator.png")
        self.pxTurnCoordinatorDrone = QPixmap("BankAngleDrone.png")
        self.pxCompass = QPixmap("Compass.png")

        # Göstergelerin alınan verilere göre hareketi burada sağlanır. 
        newAirSpeed = self.pxAirspeedArrow.transformed(QTransform().rotate(airspeed*4.5-45),QtCore.Qt.SmoothTransformation)
        newAltitude = self.pxAltitudeArrow.transformed(QTransform().rotate((altitude/10)*36+90),QtCore.Qt.SmoothTransformation)
        newAltitude2 = self.pxAltitudeSmallArrow.transformed(QTransform().rotate((altitude/100)*36+90),QtCore.Qt.SmoothTransformation)
        newCompass = self.pxCompass.transformed(QTransform().rotate(-comp),QtCore.Qt.SmoothTransformation)
        newVertical = self.pxVerticalSpeedArrow.transformed(QTransform().rotate(-(15*vertic)),QtCore.Qt.SmoothTransformation)
        newAttitude = self.pxAttitudeIndicator.transformed(QTransform().rotate(roll*57),QtCore.Qt.SmoothTransformation)
        newtTurnCoordinator= self.pxTurnCoordinatorDrone.transformed(QTransform().rotate(roll*8.1),QtCore.Qt.SmoothTransformation)
        self.arrowAirSpeed.setPixmap(newAirSpeed)
        self.arrowAltimeter.setPixmap(newAltitude)
        self.arrowSmall.setPixmap(newAltitude2)
        self.compass.setPixmap(newCompass)
        self.arrowVerticalSpeed.setPixmap(newVertical)
        self.turnCoordDrone.setPixmap(newtTurnCoordinator)
        self.attitudeIndicator.setGeometry(QtCore.QRect(20, (-4+int((pitch*60)))*2.5,1250,1250))
        self.attitudeIndicator.setPixmap(newAttitude)

"""
    Bu fonksiyon Linux veya Windows işletim sistemindeki portları kontrol ederek 
    pixhawkın bağlı olduğu portu bulur. Bu portlar üzerinde bir cihaz bulunursa bağlantı kurulur.

"""
def connectDrone():
    if sys.platform.startswith('win'):
        avaliable_ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        avaliable_ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        avaliable_ports = glob.glob('/dev/tty.*')
    result = []
    for port in avaliable_ports:
        try:
            serialPort = serial.Serial(port)
            serialPort.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    connectionString=result[0]
    avesDrone = connect(connectionString,wait_ready = True,timeout=100)
    return avesDrone

if __name__ == "__main__":
    print("Baslatiliyor...")
    avesDrone=connectDrone() #Araçla bağlantı kurulur.
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow() # Ana pencere oluşturulur.
    window.show() #Oluşturulan pencere ekranda gösterilir.
    sys.exit(app.exec_())
