# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5 import QtWidgets, uic
import SplitPage

def getFile():
    dlg.lineEdit.setText(QtWidgets.QFileDialog.getOpenFileName()[0])

def split():
    path = dlg.lineEdit.text()
    start = int(dlg.lineEdit_2.text())
    end = int(dlg.lineEdit_3.text())
    name = dlg.lineEdit_4.text()
    
    SplitPage.SplitPage(path, start, end, name)

app = QtWidgets.QApplication([])
dlg = uic.loadUi("untitled.ui")

dlg.pushButton_2.clicked.connect(getFile)
dlg.pushButton.clicked.connect(split)

dlg.show()
app.exec()