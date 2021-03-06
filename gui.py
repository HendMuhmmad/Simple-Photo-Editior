# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1187, 856)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.inputimage = QtWidgets.QLabel(self.groupBox)
        self.inputimage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.inputimage.setText("")
        self.inputimage.setObjectName("inputimage")
        self.verticalLayout_6.addWidget(self.inputimage)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.outputimage = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputimage.sizePolicy().hasHeightForWidth())
        self.outputimage.setSizePolicy(sizePolicy)
        self.outputimage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.outputimage.setText("")
        self.outputimage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.outputimage.setObjectName("outputimage")
        self.horizontalLayout_14.addWidget(self.outputimage)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loadimage = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.loadimage.setFont(font)
        self.loadimage.setObjectName("loadimage")
        self.horizontalLayout_2.addWidget(self.loadimage)
        self.saveimage = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.saveimage.setFont(font)
        self.saveimage.setObjectName("saveimage")
        self.horizontalLayout_2.addWidget(self.saveimage)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.exposure_pushButton = QtWidgets.QPushButton(self.groupBox_11)
        self.exposure_pushButton.setObjectName("exposure_pushButton")
        self.horizontalLayout_12.addWidget(self.exposure_pushButton)
        self.exposure = QtWidgets.QSlider(self.groupBox_11)
        self.exposure.setOrientation(QtCore.Qt.Horizontal)
        self.exposure.setObjectName("exposure")
        self.horizontalLayout_12.addWidget(self.exposure)
        self.label_2 = QtWidgets.QLabel(self.groupBox_11)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_12.addWidget(self.label_2)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_12)
        self.verticalLayout_3.addWidget(self.groupBox_11)
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.contrast_pushButton = QtWidgets.QPushButton(self.groupBox_12)
        self.contrast_pushButton.setObjectName("contrast_pushButton")
        self.horizontalLayout_13.addWidget(self.contrast_pushButton)
        self.contrast = QtWidgets.QSlider(self.groupBox_12)
        self.contrast.setOrientation(QtCore.Qt.Horizontal)
        self.contrast.setObjectName("contrast")
        self.horizontalLayout_13.addWidget(self.contrast)
        self.contrat_label = QtWidgets.QLabel(self.groupBox_12)
        self.contrat_label.setObjectName("contrat_label")
        self.horizontalLayout_13.addWidget(self.contrat_label)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_13)
        self.verticalLayout_3.addWidget(self.groupBox_12)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tempreture_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.tempreture_pushButton.setObjectName("tempreture_pushButton")
        self.horizontalLayout_7.addWidget(self.tempreture_pushButton)
        self.tempreture = QtWidgets.QSlider(self.groupBox_4)
        self.tempreture.setOrientation(QtCore.Qt.Horizontal)
        self.tempreture.setObjectName("tempreture")
        self.horizontalLayout_7.addWidget(self.tempreture)
        self.temp_label = QtWidgets.QLabel(self.groupBox_4)
        self.temp_label.setObjectName("temp_label")
        self.horizontalLayout_7.addWidget(self.temp_label)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.saturation_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.saturation_pushButton.setObjectName("saturation_pushButton")
        self.horizontalLayout_5.addWidget(self.saturation_pushButton)
        self.saturation = QtWidgets.QSlider(self.groupBox_5)
        self.saturation.setOrientation(QtCore.Qt.Horizontal)
        self.saturation.setObjectName("saturation")
        self.horizontalLayout_5.addWidget(self.saturation)
        self.sat_label = QtWidgets.QLabel(self.groupBox_5)
        self.sat_label.setObjectName("sat_label")
        self.horizontalLayout_5.addWidget(self.sat_label)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.color_effects_pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.color_effects_pushButton.setObjectName("color_effects_pushButton")
        self.horizontalLayout_6.addWidget(self.color_effects_pushButton)
        self.coloreffects = QtWidgets.QSlider(self.groupBox_6)
        self.coloreffects.setOrientation(QtCore.Qt.Horizontal)
        self.coloreffects.setObjectName("coloreffects")
        self.horizontalLayout_6.addWidget(self.coloreffects)
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addWidget(self.groupBox_6)
        self.cartoon_pushButton = QtWidgets.QPushButton(self.tab_3)
        self.cartoon_pushButton.setObjectName("cartoon_pushButton")
        self.verticalLayout_4.addWidget(self.cartoon_pushButton)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.sharpen_pushButton = QtWidgets.QPushButton(self.groupBox_8)
        self.sharpen_pushButton.setObjectName("sharpen_pushButton")
        self.horizontalLayout_9.addWidget(self.sharpen_pushButton)
        self.sharpening = QtWidgets.QSlider(self.groupBox_8)
        self.sharpening.setOrientation(QtCore.Qt.Horizontal)
        self.sharpening.setObjectName("sharpening")
        self.horizontalLayout_9.addWidget(self.sharpening)
        self.sharp_label = QtWidgets.QLabel(self.groupBox_8)
        self.sharp_label.setObjectName("sharp_label")
        self.horizontalLayout_9.addWidget(self.sharp_label)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.smoothing_pushButton = QtWidgets.QPushButton(self.groupBox_9)
        self.smoothing_pushButton.setObjectName("smoothing_pushButton")
        self.horizontalLayout_10.addWidget(self.smoothing_pushButton)
        self.smoothing = QtWidgets.QSlider(self.groupBox_9)
        self.smoothing.setOrientation(QtCore.Qt.Horizontal)
        self.smoothing.setObjectName("smoothing")
        self.horizontalLayout_10.addWidget(self.smoothing)
        self.smooth_label = QtWidgets.QLabel(self.groupBox_9)
        self.smooth_label.setObjectName("smooth_label")
        self.horizontalLayout_10.addWidget(self.smooth_label)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_10)
        self.verticalLayout_5.addWidget(self.groupBox_9)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.vignette_pushButton = QtWidgets.QPushButton(self.groupBox_10)
        self.vignette_pushButton.setObjectName("vignette_pushButton")
        self.horizontalLayout_11.addWidget(self.vignette_pushButton)
        self.vignette = QtWidgets.QSlider(self.groupBox_10)
        self.vignette.setOrientation(QtCore.Qt.Horizontal)
        self.vignette.setObjectName("vignette")
        self.horizontalLayout_11.addWidget(self.vignette)
        self.v_label = QtWidgets.QLabel(self.groupBox_10)
        self.v_label.setObjectName("v_label")
        self.horizontalLayout_11.addWidget(self.v_label)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_11)
        self.verticalLayout_5.addWidget(self.groupBox_10)
        self.BlackandWhite = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.BlackandWhite.setFont(font)
        self.BlackandWhite.setObjectName("BlackandWhite")
        self.verticalLayout_5.addWidget(self.BlackandWhite)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.flip = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.flip.setFont(font)
        self.flip.setObjectName("flip")
        self.horizontalLayout_3.addWidget(self.flip)
        self.flip_top_down = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.flip_top_down.setFont(font)
        self.flip_top_down.setObjectName("flip_top_down")
        self.horizontalLayout_3.addWidget(self.flip_top_down)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rotate_pushButton = QtWidgets.QPushButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rotate_pushButton.setFont(font)
        self.rotate_pushButton.setObjectName("rotate_pushButton")
        self.horizontalLayout_4.addWidget(self.rotate_pushButton)
        self.rotate = QtWidgets.QSlider(self.groupBox_7)
        self.rotate.setOrientation(QtCore.Qt.Horizontal)
        self.rotate.setObjectName("rotate")
        self.horizontalLayout_4.addWidget(self.rotate)
        self.label = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addWidget(self.groupBox_7)
        self.crop = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.crop.setFont(font)
        self.crop.setObjectName("crop")
        self.verticalLayout_7.addWidget(self.crop)
        self.logo = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.logo.setFont(font)
        self.logo.setObjectName("logo")
        self.verticalLayout_7.addWidget(self.logo)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(2, 1)
        self.verticalLayout_7.setStretch(3, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_8.addWidget(self.frame)
        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1187, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Input Image"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output Image"))
        self.loadimage.setText(_translate("MainWindow", "Load Image"))
        self.saveimage.setText(_translate("MainWindow", "Save Image"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Exposure"))
        self.exposure_pushButton.setText(_translate("MainWindow", "Save"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Contrast"))
        self.contrast_pushButton.setText(_translate("MainWindow", "Save "))
        self.contrat_label.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Light editing "))
        self.groupBox_4.setTitle(_translate("MainWindow", "Temperature"))
        self.tempreture_pushButton.setText(_translate("MainWindow", "Save"))
        self.temp_label.setText(_translate("MainWindow", "0"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Saturation"))
        self.saturation_pushButton.setText(_translate("MainWindow", "Save "))
        self.sat_label.setText(_translate("MainWindow", "0"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Color Effects"))
        self.color_effects_pushButton.setText(_translate("MainWindow", "Save"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.cartoon_pushButton.setText(_translate("MainWindow", "Cartoon"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Color editing"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Sharpening"))
        self.sharpen_pushButton.setText(_translate("MainWindow", "Save"))
        self.sharp_label.setText(_translate("MainWindow", "0"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Smoothing"))
        self.smoothing_pushButton.setText(_translate("MainWindow", "Save"))
        self.smooth_label.setText(_translate("MainWindow", "0"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Vignette"))
        self.vignette_pushButton.setText(_translate("MainWindow", "Save "))
        self.v_label.setText(_translate("MainWindow", "0"))
        self.BlackandWhite.setText(_translate("MainWindow", "Black and White"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Effects"))
        self.groupBox_3.setTitle(_translate("MainWindow", "General"))
        self.flip.setText(_translate("MainWindow", "Flip RightLeft"))
        self.flip_top_down.setText(_translate("MainWindow", "Flip TopDown"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Rotate"))
        self.rotate_pushButton.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "0"))
        self.crop.setText(_translate("MainWindow", "Crop"))
        self.logo.setText(_translate("MainWindow", "Logo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
