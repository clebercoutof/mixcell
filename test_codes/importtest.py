import os 
os.sys.path.append('../QTCode')             # Path setting
import simple as mixcell


if __name__ == "__main__":
    import sys
    app = mixcell.QtGui.QApplication(sys.argv)
    MainWindow = mixcell.QtGui.QMainWindow()
    ui = mixcell.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
