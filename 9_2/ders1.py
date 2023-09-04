#pyqt5 ile tasarlanın nesnelere widget diyoruz.
#ana ekran, form ekranı, diyalog

import sys
from PyQt5 import QtWidgets

uygulama = QtWidgets.QApplication(sys.argv) # arayüze etki edecek

pencere = QtWidgets.QWidget()

pencere.show()

sys.exit((uygulama.exec()))