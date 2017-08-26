from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from IpExtractorGui import IpExtractorDialog


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        dialog = IpExtractorDialog()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
        QMessageBox.about(dialog, "Error", str(e))