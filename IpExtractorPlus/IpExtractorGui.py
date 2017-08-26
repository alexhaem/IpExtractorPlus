from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
import os
from LinksProcessor import LinksProcessor


SOURCE_FILE = r'E:\Dropbox\random files\ips.txt'
TARGET_FOLDER = r'C:\Users\IrSha\Desktop'


class IpExtractorDialog(QtWidgets.QDialog):
    def __init__(self):
        super(IpExtractorDialog, self).__init__()
        path = os.path.join("rsc" + os.sep + "gui.ui")
        uic.loadUi(path, self)
        
        # initialize connect events
        self.pushButton_browse_input.clicked.connect(self.browseInput)
        self.pushButton_browse_output.clicked.connect(self.browseOutput)
        self.pushButton_run.clicked.connect(self.processLinks)
    
        # fill out input/output paths
        input_file = self.lineEdit_input.text
        if input_file:
            self.lineEdit_input.setText(SOURCE_FILE)
    
        output_file = self.lineEdit_output.text
        if output_file:
            self.lineEdit_output.setText(TARGET_FOLDER)
            
        self.show()

        
    def browseInput(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilters(["Text files (*.txt)"])
        file_dialog.selectNameFilter("Text files (*.txt)")
        if file_dialog.exec_():
            self.lineEdit_input.setText(file_dialog.selectedFiles()[0])
         
    def browseOutput(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory").strip()
        if folder:
            self.lineEdit_output.setText(folder)

         
    def processLinks(self):
        # disable all buttons
        self.pushButton_run.setEnabled(False)
        self.pushButton_browse_input.setEnabled(False)
        self.pushButton_browse_output.setEnabled(False)
        
        # process links
        inputTxt = self.lineEdit_input.text()
        outputFolder =  self.lineEdit_output.text()
        processor = LinksProcessor()
        processor.processLinks(inputTxt, outputFolder)
        
        # enable all buttons
        self.pushButton_run.setEnabled(True)
        self.pushButton_browse_input.setEnabled(True)
        self.pushButton_browse_output.setEnabled(True)
