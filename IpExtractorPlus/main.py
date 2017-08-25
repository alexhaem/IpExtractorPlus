from PyQt5 import QtWidgets, uic
import sys, os

class IpExtractorPlus(QtWidgets.QDialog):
    def __init__(self):
        super(IpExtractorPlus, self).__init__()
        path = os.path.join("rsc" + os.sep + "gui.ui")
        uic.loadUi(path, self)
        
        self.pushButton_browse_input.clicked.connect(self.browseInput)
        self.pushButton_browse_output.clicked.connect(self.browseOutput)
        self.pushButton.clicked.connect(self.run)
    
        self.show()
        
    def browseInput(self):
        print("browse input")
         
    def browseOutput(self):
        print("browse output")
         
    def run(self):
        print("run")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = IpExtractorPlus()
    sys.exit(app.exec_())
