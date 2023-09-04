import sys
from kitapekle import KitapEkleEkrani
from anaekran_ui import Ui_AnaEkran
from PyQt5.QtWidgets import *

class Anaekran(QMainWindow,Ui_AnaEkran):
    
    def __init__(self,k_id):
        super(Anaekran,self).__init__()
        self.k_id = k_id
        self.karsilama()

    def karsilama(self):
        self.setupUi(self)
        self.menuKitap_Ekle.triggered.connect(self.kitap_ekle)    #menü ise triggered
        self.menuKitap_Listesi.triggered.connect(self.kitap_listele)
        self.menuSil.triggered.connect(self.kitap_silme)
        self.menuKitap_Guncelle.triggered.connect(self.kitap_guncelle)
        self.menuCikis.triggered.connect(self.cikis)


    def kitap_ekle(self):
        self.setCentralWidget(KitapEkleEkrani())

    def kitap_listele(self):
        #self.setupUi(self) olsa da olmasa da çalışıyor
        self.karsilama()

    def kitap_silme(self):
        self.setCentralWidget()

    def kitap_guncelle(self):
        print("güncelle tıklandı")

    def cikis(self):
        print("çıkış tıklandı")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Anaekran()
    pencere.show()
    sys.exit(app.exec())