# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""




######sys######
import sys

######UI######
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from Ui_min_win import Ui_MainWindow



#txt to list
def txt2list(txt_path):
    txt_list = []
    with open(txt_path) as f :
        for line in f:
            txt_list.append(line.split('\n')[0])
    return txt_list



class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    camb_imgs_list = []
    score_idices = []
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
    
    @pyqtSignature("")  
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        测试按钮槽函数
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        #print  'a'
        print  self.comboBox.currentText()
        
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
      
        #self.graphicsView.setStyleSheet(("border-image: url(:/pic/2.jpg);"))
        
        #适应label大小展示图片
        #默认路径，可修改："/home/nikoong/Algorithm_test/PyQt/gui/demo/data"
        file_name = QtGui.QFileDialog.getOpenFileName(self, u'选择图像', r"/home/nikoong/Algorithm_test/PyQt/gui/demo/data")
        print "1"
        """
        try:
            file = open(file_name)
            data = file.read()
        except UnicodeDecodeError:
            data ="无效的图片"
        except IOError :
            data =""        
        """
        self.label_5.setScaledContents(True)
        pixmap = QtGui.QPixmap(file_name)
        self.label_5.setPixmap(pixmap)
        self.lineEdit.setText(unicode(file_name))
        #print unicode(self.lineEdit.text())
    
       
    @pyqtSignature("")

    def on_pushButton_2_clicked(self):
        """
        # 搜索按钮负责主要的逻辑
        """
        #意思是：当"选择图像库"和"选择算法"按钮都为1时。这个判断语句是为后期扩展预留的。
        if self.comboBox.currentText() == "1" and self.comboBox_2.currentText() == "1":

            #需要查找的人物图片，是通过on_pushButton_3_clicked函数得到的，这里直接调用。
            query_pathfile_name = unicode(self.lineEdit.text())
            #print query_pathfile_name;
            if query_pathfile_name == "/home/nikoong/Algorithm_test/PyQt/gui/demo/data/b.jpg":
                camb_imgs_list = txt2list("/home/nikoong/Algorithm_test/PyQt/gui/demo/data/camb_imgs_list_b.txt")
            else:
                camb_imgs_list = txt2list("/home/nikoong/Algorithm_test/PyQt/gui/demo/data/camb_imgs_list_a.txt")


        #将50张图片输出。
        self.label_71.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[0])
        self.label_71.setPixmap(pixmap)

        self.label_7.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[1])
        self.label_7.setPixmap(pixmap)
        
        self.label_8.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[2])
        self.label_8.setPixmap(pixmap)
        
        self.label_9.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[3])
        self.label_9.setPixmap(pixmap)
        
        self.label_10.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[4])
        self.label_10.setPixmap(pixmap)
        
        self.label_11.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[5])
        self.label_11.setPixmap(pixmap)
        
        self.label_12.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[6])
        self.label_12.setPixmap(pixmap)
        
        self.label_13.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[7])
        self.label_13.setPixmap(pixmap)
        
        self.label_14.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[8])
        self.label_14.setPixmap(pixmap)
        
        self.label_15.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[9])
        self.label_15.setPixmap(pixmap)
        
        self.label_16.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[10])
        self.label_16.setPixmap(pixmap)
        
        self.label_17.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[11])
        self.label_17.setPixmap(pixmap)
        
        self.label_18.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[12])
        self.label_18.setPixmap(pixmap)
        
        self.label_19.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[13])
        self.label_19.setPixmap(pixmap)
        
        self.label_20.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[14])
        self.label_20.setPixmap(pixmap)
        
        self.label_21.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[15])
        self.label_21.setPixmap(pixmap)
        
        self.label_37.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[16])
        self.label_37.setPixmap(pixmap)
        
        self.label_38.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[17])
        self.label_38.setPixmap(pixmap)
        
        self.label_39.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[18])
        self.label_39.setPixmap(pixmap)
        
        self.label_40.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[19])
        self.label_40.setPixmap(pixmap)
        
        self.label_41.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[20])
        self.label_41.setPixmap(pixmap)
        
        self.label_42.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[21])
        self.label_42.setPixmap(pixmap)
        
        self.label_43.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[22])
        self.label_43.setPixmap(pixmap)
        
        self.label_44.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[23])
        self.label_44.setPixmap(pixmap)
        
        self.label_45.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[24])
        self.label_45.setPixmap(pixmap)
        
        self.label_46.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[25])
        self.label_46.setPixmap(pixmap)
        
        self.label_47.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[26])
        self.label_47.setPixmap(pixmap)
        
        self.label_48.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[27])
        self.label_48.setPixmap(pixmap)
        
        self.label_49.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[28])
        self.label_49.setPixmap(pixmap)
        
        self.label_50.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[29])
        self.label_50.setPixmap(pixmap)
        
        self.label_51.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[30])
        self.label_51.setPixmap(pixmap)
        
        self.label_52.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[31])
        self.label_52.setPixmap(pixmap)
        
        self.label_53.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[32])
        self.label_53.setPixmap(pixmap)
        
        self.label_54.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[33])
        self.label_54.setPixmap(pixmap)
        
        self.label_55.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[34])
        self.label_55.setPixmap(pixmap)
        
        self.label_56.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[35])
        self.label_56.setPixmap(pixmap)
        
        self.label_57.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[36])
        self.label_57.setPixmap(pixmap)
        
        self.label_58.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[37])
        self.label_58.setPixmap(pixmap)
        
        self.label_59.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[38])
        self.label_59.setPixmap(pixmap)
        
        self.label_60.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[39])
        self.label_60.setPixmap(pixmap)
        
        self.label_61.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[40])
        self.label_61.setPixmap(pixmap)

        self.label_62.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[41])
        self.label_62.setPixmap(pixmap)
        
        self.label_63.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[42])
        self.label_63.setPixmap(pixmap)
        
        self.label_64.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[43])
        self.label_64.setPixmap(pixmap)
        
        self.label_65.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[44])
        self.label_65.setPixmap(pixmap)
        
        self.label_66.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[45])
        self.label_66.setPixmap(pixmap)
        
        self.label_67.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[46])
        self.label_67.setPixmap(pixmap)
        
        self.label_68.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[47])
        self.label_68.setPixmap(pixmap)
        
        self.label_69.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[48])
        self.label_69.setPixmap(pixmap)
        
        self.label_70.setScaledContents(True)
        pixmap = QtGui.QPixmap(camb_imgs_list[49])
        self.label_70.setPixmap(pixmap)
        

                
              
                
              
    @pyqtSignature("")
    def on_pushButton_8_clicked(self):
            self.label_7.setScaledContents(True)
            pixmap = QtGui.QPixmap(camb_imgs_list[2])
            self.label_7.setPixmap(pixmap)
            
        
                
                
                
             
        

    
    

if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    

