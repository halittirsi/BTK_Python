from kitapekle_ui import Ui_KitapEkleForm
from PyQt5.QtWidgets import *
import sys
import 

class KitapEkleEkrani(QWidget, Ui_KitapEkleForm):

    def __init__(self,k_id):
        super(KitapEkleEkrani,self).__init__()
        self.k_id = k_id
        self.fbaslat()
        self.setupUi(self)
        
    def fbaslat(self):
        self.setupUi(self)
        self.kitapKayitButton.clicked(self.kitap_ekle)

    def kitap_ekle(self):
        k_adi = self.kitapAdiLineEdit.text()
        k_yazari = self.kitapYazariLineEdit.text()
        k_durum = self.okunmaDurumuCheckBox.checkState()
        k_begeni = self.beEniDurumuComboBox.itemText()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = KitapEkleEkrani()
    pencere.show()
    sys.exit(app.exec())