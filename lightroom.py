import sys
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QFileDialog  #,QApplication ,QDialog ,QWidget
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
from PIL import Image, ImageEnhance
# import cv2 as cv
import numpy as np
from gui import Ui_MainWindow
from crop import Ui_Dialog
import os

class Main(QtWidgets.QMainWindow ,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loadimage.clicked.connect(lambda _: self.click_load_image())
        self.ui.saveimage.clicked.connect(lambda : self.click_save_image())
        self.ui.BlackandWhite.clicked.connect(lambda : self.BlackAndWhite())
        
        self.ui.sharpening.valueChanged.connect(lambda: self.Sharpen())
        self.ui.sharpening.setMinimum(0)
        self.ui.sharpening.setMaximum(100)
        self.ui.smoothing.valueChanged.connect(lambda: self.SmoothBlur())
        self.ui.smoothing.setMinimum(0)
        self.ui.smoothing.setMaximum(100)
        self.ui.vignette.valueChanged.connect(lambda: self.Vignette())
        self.ui.vignette.setMinimum(0)
        self.ui.vignette.setMaximum(100)
    
        self.ui.contrast.valueChanged.connect(lambda : self.contrastExposure(self.ui.contrast.value()/100,0))
        self.ui.contrast.setMinimum(0)
        self.ui.contrast.setMaximum(100)
        self.ui.exposure.valueChanged.connect(lambda : self.contrastExposure(0,self.ui.exposure.value()))
        self.ui.exposure.setMinimum(0)
        self.ui.exposure.setMaximum(100)
        self.ui.rotate.valueChanged.connect(lambda : self.rotate())
        self.ui.rotate.setMinimum(0)
        self.ui.rotate.setMaximum(360)
        self.ui.flip.clicked.connect(lambda : self. flip_right_left_image())
        self.ui.flip_top_down.clicked.connect(lambda : self. flip_top_down_image())
        self.ui.tempreture.valueChanged.connect(lambda: self.Temp())
        self.ui.tempreture.setMinimum(-100)
        self.ui.tempreture.setMaximum(100)
        self.ui.logo.clicked.connect(lambda : self.LOGO())
       
        self.ui.coloreffects.valueChanged.connect(lambda : self.Effects())
        self.ui.coloreffects.setMinimum(0)
        self.ui.coloreffects.setMaximum(13)
        
        self.ui.saturation.valueChanged.connect(lambda : self.saturation())
        self.ui.saturation.setMinimum(-300)
        self.ui.saturation.setMaximum(300)

        self.ui.crop.clicked.connect(lambda: self.click_Crop())
        
        self.ui.cartoon_pushButton.clicked.connect(lambda : self. cartoon())
        self.img_format=None
        self.img_name=None
        self.imagePath = None
        self.img_format = None
        # self.image =None
        # if self.image is not None:
        #     self.img_name = self.image.split('\\')[-1].split(".")[0]
        #     self.img_format = self.image.split('\\')[-1].split(".")[1]
        
        # self.image_copy =None
        self.op_size = None
        self.ip_size = None
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.cwd = self.cwd.replace("\\","/")
        self.ui.sharpen_pushButton.clicked.connect(lambda : self.save_edit(self.cwd+"/sharpened-image."+self.img_format))
        self.ui.smoothing_pushButton.clicked.connect(lambda : self.save_edit(self.cwd+"/smoothed-image."+self.img_format))
        self.ui.vignette_pushButton.clicked.connect(lambda : self.save_edit(self.cwd+"/vignette-image."+self.img_format))

        self.ui.tempreture_pushButton.clicked.connect(lambda : self.save_edit(self.cwd+"/temp_image."+self.img_format))
        self.ui.color_effects_pushButton.clicked.connect(lambda : self.save_edit(self.cwd+"/effected_image."+self.img_format))
        self.ui.saturation_pushButton.clicked.connect(lambda : self.save_edit(self.cwd+"/saturation_image."+self.img_format))

        self.ui.exposure_pushButton.clicked.connect(lambda : self.save_edit(self.cwd+"/Exposure-image."+self.img_format))
        self.ui.contrast_pushButton.clicked.connect(lambda : self.save_edit(self.cwd+"/contrast-image."+self.img_format))
        self.ui.rotate_pushButton.clicked.connect(lambda : self.save_edit(self.cwd+"/rotated-image."+self.img_format))
    def save_edit(self,path):
        self.imagePath = path
        # print(self.imagePath)

    

    def click_load_image(self):

        files, _ = QFileDialog.getOpenFileNames(self, "Choose Image File", "../",
                                                "Image Files (*.jpg *.png *.jpeg *.ico);;All Files (*)")
        if files:
            self.imagePath=str(files[0])
            self.img_format = self.imagePath.split('\\')[-1].split(".")[1]
            pixmap= QPixmap(self.imagePath)
            # self.ui.inputimage.setScaledContents(True)
            self.op_size = self.ui.outputimage.size()
            self.ip_size = self.ui.inputimage.size()
            scaled = pixmap.scaled(self.ip_size)#,QtCore.Qt.KeepAspectRatio)
            self.ui.inputimage.setPixmap(scaled)
            # self.image=cv2.imread(self.imagePath)
            # self.image_copy=self.image.copy()

    def  click_save_image(self):
        file, _ = QFileDialog.getSaveFileName(self, 'Save File',"../","Image Files (*.png *.jpeg *.ico);;All Files (*)")
        if file:
            final_image = cv2.imread(self.imagePath)
            cv2.imwrite(file,final_image)
    
    #img type
    #cropping direction
    def click_Crop(self):
        pass
    
    def Sharpen(self):
        pass

    def SmoothBlur(self):
        pass

    def Vignette(self):
        pass

    def BlackAndWhite(self):
        pass

    def contrastExposure(self):
        pass

    def rotate(self):
        pass

    def flip_right_left_image(self):
        pass

    def flip_top_down_image(self):
        pass

    def Temp(self):
        pass

    def LOGO(self):
        pass

    def Effects(self): 
        pass

    def saturation(self):
        pass

    def cartoon(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # styleSheet="styles.css"
    # with open(styleSheet,"r") as f:
    #     app.setStyleSheet(f.read())
    MainWindow=Main()
    MainWindow.show()
    sys.exit(app.exec_())   