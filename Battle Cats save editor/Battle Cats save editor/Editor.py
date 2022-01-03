from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os, os.path, sys

catAmount = 0
Savepaths = []
gameVer = ""
version = '2.38.1'

Color = {
"Default": "\x1b[39m",
"Black": "\x1b[30m",
"Red": "\x1b[31m",
"Green": "\x1b[32m",
"Yellow": "\x1b[33m",
"Blue": "\x1b[34m",
"Magenta": "\x1b[35m",
"Cyan": "\x1b[36m",
"LightGray": "\x1b[37m",
"DarkGray": "\x1b[90m",
"LightRed": "\x1b[91m",
"LightGreen": "\x1b[92m",
"LightYellow": "\x1b[93m",
"LightBlue": "\x1b[94m",
"LightMagenta": "\x1b[95m",
"LightCyan": "\x1b[96m",
"White": "\x1b[97m",
}

def SelSave():
    dlg = QFileDialog()
    dlg.setFileMode(QFileDialog.ExistingFiles)
    dlg.setNameFilters(["battle cats save (*.*)",])

    if dlg.exec_() == QDialog.Accepted:
        fileToOpen = dlg.selectedFiles()
        for i in range(len(fileToOpen)):
            print(f"{Color['White']}Save: {Color['Green']}\"{os.path.basename(fileToOpen[i])}\"{Color['White']}");
        Savepaths = fileToOpen
    else:
        print("Please select your save\n")
        SelSave()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        SelSave()
        Options()
    except Exception as e:
        print("An error has occurred\nPlease report this in #bug-reports:")
        print(e)
        input("Press enter to exit")
        quit()
