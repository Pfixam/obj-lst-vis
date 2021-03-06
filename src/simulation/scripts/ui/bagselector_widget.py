'''
    this is a widget to import Rosbag files 
'''

import os
from python_qt_binding import QtCore, QtGui
from python_qt_binding.QtWidgets import (QWidget, QLineEdit, QPushButton, 
                                         QHBoxLayout, QVBoxLayout, QFileDialog)

class BagWidget(QWidget):  
    '''
        contains two selectors two determine 
        which bag files should be imported
    '''  
    def __init__(self, parent=None):
        super(BagWidget, self).__init__()
        self.parent = parent
                
        # create elements
        self.bagSelector1 = BagSelector('ground truth bag file')
        self.bagSelector2 = BagSelector('camera data bag file')
        
        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.bagSelector1)
        layout.addWidget(self.bagSelector2)
        self.setLayout(layout)
        
    def getBagFiles(self):
        return [self.bagSelector1.fileName, self.bagSelector2.fileName]
    
class BagSelector(QWidget):
    '''
        one line for selecting one bag file
        contains a line edit which displays the filename
        and a button which opens a file dialog 
    '''
    def __init__(self, btnText):
        super(BagSelector, self).__init__()
        
        # init the elements
        self.bagEdit = QLineEdit()
        self.bagBtn = QPushButton(btnText)
        
        # connect the signals to the slots
        self.bagEdit.textChanged.connect(self.pathChanged)        
        self.bagBtn.clicked.connect(self.btnClicked)
        
        self.fileName = ""
        
        # layout
        layout = QHBoxLayout()
        layout.addWidget(self.bagEdit)
        layout.addWidget(self.bagBtn)
        self.setLayout(layout)
        
        
    def btnClicked(self):
        '''
            a slot which is called when the button is clicked
        '''
        cwd = os.getcwd() # current working directory
        fileTupel = QFileDialog.getOpenFileName(self, 'Select file', cwd, "Bag files (*.bag)")
        self.fileName = fileTupel[0] 
        self.bagEdit.setText(self.fileName) # print filename to lineEdit
        
        
    def pathChanged(self):
        '''
            a slot which is called when the text in the line edit 
            is changed manually
        '''
        self.fileName = self.bagEdit.text()
    
