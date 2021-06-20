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


class Crop(QtWidgets.QDialog ,Ui_Dialog):
    def __init__(self,path, parent=None):
        super(Crop, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.path = path
        self.crop = False
        self.ui.save.accepted.connect(lambda : self.crop_slot())
        self.ui.save.rejected.connect(lambda : self.no_crop())
        # self.ui..clicked.connect(lambda : self.click_load_image())

    def crop_slot(self):
        self.crop = True
        self.close()

    def no_crop(self):
        self.crop=False
        self.close()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        pixmap = QPixmap(self.path)
        self.setGeometry(500,100,pixmap.width(),pixmap.height())
        qp.drawPixmap(0,0,pixmap.width(),pixmap.height(),pixmap)
        br = QtGui.QBrush(QtGui.QColor(100, 10, 10, 40))  
        qp.setBrush(br)   
        qp.drawRect(QtCore.QRect(self.begin, self.end))       

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()


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
        dialog=Crop(self.imagePath)
        
        dialog.exec_()
        if dialog.crop:
            img = Image.open(self.imagePath)
            x1 = dialog.begin.x()
            y1 = dialog.begin.y()
            x2 = dialog.end.x()
            y2 = dialog.end.y()
            im1 = img.crop((x1, y1, x2, y2))
            im1.save('cropped_image.'+self.img_format)
            pixmap= QPixmap('cropped_image.'+self.img_format)
            scaled = pixmap.scaled(self.op_size)
            self.ui.outputimage.setPixmap(scaled)
            # self.ui.outputimage.setScaledContents(True)
            # self.ui.outputimage.setPixmap(QPixmap(pixmap))
            self.imagePath = self.cwd+"/cropped_image."+self.img_format
    
    def Sharpen(self):
        sharpenfactor = self.ui.sharpening.value() 
        self.ui.sharp_label.setText(str(sharpenfactor))
        sharpenfactor=sharpenfactor/100
        # image=self.image_copy

        im = Image.open(self.imagePath)
        enhancer = ImageEnhance.Sharpness(im)
        if(sharpenfactor*10>0):
            im_s_1 = enhancer.enhance(sharpenfactor*10)
            im_s_1.save('sharpened-image.'+self.img_format)
            # new_image=cv.imread('sharpened-image.png')
        # else:
        #     new_image=image

        pixmap= QPixmap('sharpened-image.'+self.img_format)
        scaled = pixmap.scaled(self.op_size)#,QtCore.Qt.KeepAspectRatio)
        self.ui.outputimage.setPixmap(scaled)

    def SmoothBlur(self):
        blur =self.ui.smoothing.value()
        self.ui.smooth_label.setText(str(blur))
        blur=blur/100
        image=cv2.imread(self.imagePath)
        s=image.shape
        MaxFilterSize=min(s[:1])
        FilterSize =int(MaxFilterSize*blur/10)
        if(FilterSize):
            new_image_s_1=cv2.blur(image,(FilterSize,FilterSize),0)
            new_image_s_1 =cv2.imwrite('smoothed-image.'+self.img_format,new_image_s_1)
        #     new_image=cv.imread('smoothed-image.png')
        # else:
        #     new_image=image
        
        pixmap= QPixmap('smoothed-image.'+self.img_format)
        scaled = pixmap.scaled(self.op_size)
        self.ui.outputimage.setPixmap(scaled)

    def Vignette(self):
        factor=self.ui.vignette.value()
        self.ui.v_label.setText(str(factor))
        factor=(factor+50)/100

        image=cv2.imread(self.imagePath)

        rows, cols, = image.shape[:2]
        # print(rows)
        # print(cols)
        # generating vignette mask using Gaussian kernels
        factorx=int(factor*cols)
        factory=int(factor*rows)
        kernel_x = cv2.getGaussianKernel(cols,factorx)
        kernel_y = cv2.getGaussianKernel(rows,factory)
        kernel = kernel_y * kernel_x.T
        mask = 255 * kernel / np.linalg.norm(kernel)
        output = np.copy(image)
        # print(mask)
        # applying the mask to each channel in the input image
        for i in range(3):
            # print(i)
            output[:,:,i] = output[:,:,i] * mask
   
        cv2.imwrite('vignette-image.'+self.img_format,output)
        # new_image=cv.imread('vignette-image.png')

        pixmap= QPixmap('vignette-image.'+self.img_format)
        scaled = pixmap.scaled(self.op_size)
        self.ui.outputimage.setPixmap(scaled)

    def BlackAndWhite(self): 
        originalImage=cv2.imread(self.imagePath)
        grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
        cv2.imwrite('blackandwhite-image.'+self.img_format,blackAndWhiteImage)
        # new_image=cv.imread('blackandwhite-image.png')
        pixmap= QPixmap('blackandwhite-image.'+self.img_format)
        scaled = pixmap.scaled(self.op_size)
        self.ui.outputimage.setPixmap(scaled)
        self.imagePath = self.cwd+"/blackandwhite-image."+self.img_format
            

    def contrastExposure(self,contrast,brightness):
        alpha = 1+2.0*contrast # Contrast control (1.0-3.0)
        beta = brightness#*100 # Brightness control (0-100)
        image = cv2.imread(self.imagePath)
        adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        file_name = ""
        if brightness == 0:
            file_name = "contrast-image."+self.img_format
            self.ui.contrat_label.setText(str(int(contrast*100)))
        elif contrast == 0:
            file_name = "Exposure-image."+self.img_format
            self.ui.label_2.setText(str(brightness))

        cv2.imwrite(file_name,adjusted)
        pixmap= QPixmap(file_name)
        scaled = pixmap.scaled(self.op_size)
        self.ui.outputimage.setPixmap(scaled)
        
    def rotate(self):
        degrees_to_rotate=self.ui.rotate.value()
        self.ui.label.setText(str(degrees_to_rotate))
        # image=self.image_copy
        image = Image.open(self.imagePath)
        rotated_image = image.rotate(degrees_to_rotate) 
        
        rotated_image.save('rotated-image.'+self.img_format)
        # new_image=cv.imread('rotated-image.png')
        
        pixmap= QPixmap('rotated-image.'+self.img_format)
        scaled = pixmap.scaled(self.op_size)
        self.ui.outputimage.setPixmap(scaled)
               

    def flip_right_left_image(self):
        # image=self.image_copy
        image = Image.open(self.imagePath)
        image = image.convert('RGB')
        rotated_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        rotated_image.save('Mirrored_image.'+self.img_format) 
        # rotated_image=cv.imread('Mirrored_image.png') 
       
        pixmap= QPixmap('Mirrored_image.'+self.img_format)
        scaled = pixmap.scaled(self.op_size)
        self.ui.outputimage.setPixmap(scaled)
        self.imagePath = self.cwd+"/Mirrored_image."+self.img_format
    
    def flip_top_down_image(self):
        # image=self.image_copy
        image = Image.open(self.imagePath)
        image = image.convert('RGB')
        rotated_image1 = image.transpose(Image.FLIP_TOP_BOTTOM)
        rotated_image1.save('Mirrored_image1.'+self.img_format) 
        # rotated_image1=cv.imread('Mirrored_image1.png')
        pixmap= QPixmap('Mirrored_image1.'+self.img_format)
        scaled = pixmap.scaled(self.op_size)
        self.ui.outputimage.setPixmap(scaled)  
        self.imagePath = self.cwd+"/Mirrored_image1."+self.img_format

    #Temperature Function
    def Temp(self):
        temperaturedfactor =self.ui.tempreture.value()
        self.ui.temp_label.setText(str(temperaturedfactor))
        temperaturedfactor=temperaturedfactor/100
      
        im = Image.open(self.imagePath)
        im = im.convert('RGB')
        filter = ImageEnhance.Color(im) 
        if(temperaturedfactor*10>0): 
            im_s_1=filter.enhance(temperaturedfactor*10)       #Hotted image 
            im_s_1.save('temp_image.'+self.img_format);         #save  image
             
        else: 
            im_s_2=filter.enhance(temperaturedfactor*10)       #cooled image
            im_s_2.save('temp_image.'+self.img_format);        #save  image
             
        
        pixmap= QPixmap('temp_image.'+self.img_format)
        scaled = pixmap.scaled(self.op_size)
        self.ui.outputimage.setPixmap(scaled)

    #LOGO Function
    def LOGO(self):
        
        im = Image.open(self.imagePath) 
        im = im.convert('RGB')       
        
        lo = Image.open('logo.PNG')

        im_copy = im.copy()

        position = ((im_copy.width - lo.width), (im_copy.height - lo.height))    #calculate position for puting logo in image itself

        im_copy.paste(lo, position)

        im_copy.save('looged_image.'+self.img_format)             #save image
         
        pixmap= QPixmap('looged_image.'+self.img_format)
        scaled = pixmap.scaled(self.op_size)
        self.ui.outputimage.setPixmap(scaled)
        self.imagePath = self.cwd+"/looged_image."+self.img_format

    # Effects Function Using ColorMap
    def Effects(self): 
        number=self.ui.coloreffects.value()
        self.ui.label_4.setText(str(number))
        
        
        im_gray = cv2.imread(self.imagePath,cv2.IMREAD_GRAYSCALE)      #convert image into gray scale image
        if number==1:
         im_color= cv2.applyColorMap(im_gray,cv2.COLORMAP_AUTUMN) #COLORMAP_AUTUMN
        elif number==2: 
          im_color= cv2.applyColorMap(im_gray,cv2.COLORMAP_BONE)  #COLORMAP_BONE
        elif number==3: 
          im_color= cv2.applyColorMap(im_gray,cv2.COLORMAP_JET)   #COLORMAP_JET
        elif number==4: 
          im_color= cv2.applyColorMap(im_gray,cv2.COLORMAP_WINTER)  #COLORMAP_WINTER
        elif number==5: 
          im_color= cv2.applyColorMap(im_gray,cv2.COLORMAP_RAINBOW)  #COLORMAP_RAINBOW
        elif number==6: 
          im_color= cv2.applyColorMap(im_gray,cv2.COLORMAP_OCEAN)    #COLORMAP_OCEAN
        elif number==7: 
          im_color= cv2.applyColorMap(im_gray,cv2.COLORMAP_SUMMER)    #COLORMAP_SUMMER
        elif number==8: 
          im_color= cv2.applyColorMap(im_gray,cv2.COLORMAP_SPRING)     #COLORMAP_SPRING
        elif number==9: 
          im_color= cv2.applyColorMap(im_gray,cv2.COLORMAP_COOL)     #COLORMAP_COOL
        elif number==10: 
          im_color= cv2.applyColorMap(im_gray,cv2.COLORMAP_HSV)      #COLORMAP_HSV
        elif number==11: 
          im_color= cv2.applyColorMap(im_gray,cv2.COLORMAP_PINK)      #COLORMAP_PINK
        elif number==12: 
          im_color= cv2.applyColorMap(im_gray,cv2.COLORMAP_HOT)    #COLORMAP_HOT  
        elif number==13 : 
          im_color=im_gray                                         #gray scale image
        else:
            im_color = cv2.imread(self.imagePath)
            
        
        im_color =cv2.imwrite('effected_image.'+self.img_format,im_color) #save  image
        
        pixmap= QPixmap('effected_image.'+self.img_format)
        scaled = pixmap.scaled(self.op_size)
        self.ui.outputimage.setPixmap(scaled)

    #Saturation Function to enhance image
    def saturation(self):
        # range from -300 to 300 
        value=self.ui.saturation.value()
        self.ui.sat_label.setText(str(value))
        image =cv2.imread(self.imagePath)
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype("float32")
        (h, s, v) = cv2.split(image_hsv)
        s= s+value
        s = np.clip(s, 0, 255)
        image_hsv = cv2.merge([h, s, v])
        new_img = cv2.cvtColor(image_hsv.astype("uint8"), cv2.COLOR_HSV2BGR) 
        new_img =cv2.imwrite('saturation_image.'+self.img_format,new_img)      #save  image
        
        
        pixmap= QPixmap('saturation_image.'+self.img_format)
        scaled = pixmap.scaled(self.op_size)
        self.ui.outputimage.setPixmap(scaled)

    #Cartoon Function
    def cartoon(self):
        cartoon_image = cv2.imread(self.imagePath)

        gray_image = cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.medianBlur(gray_image,7)                               #apply median blur to reduce image noise in gray scale image
        edges = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_MEAN_C, 
                                        cv2.THRESH_BINARY,9,2)                  #apply edge mask from gray scale image by adaptive thresholding


        color = cv2.bilateralFilter(cartoon_image, 9, 9, 7)                     #apply bilateral_filter
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        cv2.imwrite('cartoon-image.'+self.img_format,cartoon)                   #save  image
         
        
        pixmap= QPixmap('cartoon-image.'+self.img_format)
        scaled = pixmap.scaled(self.op_size)
        self.ui.outputimage.setPixmap(scaled)
        self.imagePath = self.cwd+"/cartoon-image."+self.img_format  


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # styleSheet="styles.css"
    # with open(styleSheet,"r") as f:
    #     app.setStyleSheet(f.read())
    MainWindow=Main()
    MainWindow.show()
    sys.exit(app.exec_())   