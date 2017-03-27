import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(50,50,500,300)
window.setWindowTitle("tutorial")
window.show()
print("tey")

