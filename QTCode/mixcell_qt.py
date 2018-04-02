#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Cleber de Souza Couto Filho (clebercoutof@gmail.com)

from PyQt4 import QtCore, QtGui

import os
os.sys.path.append('../source_code/')             # Path setting
import source_code as mixcell

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    """QT Class with the interface and the connections"""

    #Creating all the variables that will be used as argument of dynamixel functions
    def __init__(self):
        self.baudrates_search_list = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Mixcell"))
        MainWindow.resize(1051, 587)
        MainWindow.setMinimumSize(QtCore.QSize(1051, 587))
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.framesearch = QtGui.QFrame(self.centralwidget)
        self.framesearch.setFrameShape(QtGui.QFrame.NoFrame)
        self.framesearch.setFrameShadow(QtGui.QFrame.Raised)
        self.framesearch.setObjectName(_fromUtf8("framesearch"))
        self.gridLayout = QtGui.QGridLayout(self.framesearch)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.id_search_min = QtGui.QSpinBox(self.framesearch)
        self.id_search_min.setAccelerated(True)
        self.id_search_min.setMinimum(1)
        self.id_search_min.setMaximum(252)
        self.id_search_min.setObjectName(_fromUtf8("id_search_min"))
        self.horizontalLayout.addWidget(self.id_search_min)
        self.label_4 = QtGui.QLabel(self.framesearch)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.id_search_max = QtGui.QSpinBox(self.framesearch)
        self.id_search_max.setAccelerated(True)
        self.id_search_max.setMinimum(1)
        self.id_search_max.setMaximum(252)
        self.id_search_max.setSingleStep(1)
        self.id_search_max.setObjectName(_fromUtf8("id_search_max"))
        self.horizontalLayout.addWidget(self.id_search_max)
        self.label_5 = QtGui.QLabel(self.framesearch)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.portttxt = QtGui.QLabel(self.framesearch)
        self.portttxt.setObjectName(_fromUtf8("portttxt"))
        self.gridLayout.addWidget(self.portttxt, 1, 0, 1, 1)
        self.port_combox = QtGui.QComboBox(self.framesearch)
        self.port_combox.setObjectName(_fromUtf8("port_combox"))
        self.port_combox.addItem(_fromUtf8(""))
        self.port_combox.addItem(_fromUtf8(""))
        self.port_combox.addItem(_fromUtf8(""))
        self.port_combox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.port_combox, 2, 0, 1, 1)
        self.BAUDRATEtxt = QtGui.QLabel(self.framesearch)
        self.BAUDRATEtxt.setObjectName(_fromUtf8("BAUDRATEtxt"))
        self.gridLayout.addWidget(self.BAUDRATEtxt, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.scan_btn = QtGui.QPushButton(self.framesearch)
        self.scan_btn.setMinimumSize(QtCore.QSize(266, 27))
        self.scan_btn.setMaximumSize(QtCore.QSize(266, 27))
        self.scan_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scan_btn.setStyleSheet(_fromUtf8("background-image: url(:/testebutton.jpg);"))
        self.scan_btn.setObjectName(_fromUtf8("scan_btn"))
        self.horizontalLayout_5.addWidget(self.scan_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.baudrate_list = QtGui.QListWidget(self.framesearch)
        self.baudrate_list.setFrameShape(QtGui.QFrame.StyledPanel)
        self.baudrate_list.setFrameShadow(QtGui.QFrame.Sunken)
        self.baudrate_list.setLineWidth(0)
        self.baudrate_list.setMidLineWidth(0)
        self.baudrate_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.baudrate_list.setDragEnabled(False)
        self.baudrate_list.setDragDropOverwriteMode(False)
        self.baudrate_list.setMovement(QtGui.QListView.Static)
        self.baudrate_list.setFlow(QtGui.QListView.TopToBottom)
        self.baudrate_list.setViewMode(QtGui.QListView.ListMode)
        self.baudrate_list.setUniformItemSizes(False)
        self.baudrate_list.setWordWrap(False)
        self.baudrate_list.setObjectName(_fromUtf8("baudrate_list"))
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.baudrate_list.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.baudrate_list.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.baudrate_list.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.baudrate_list.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.baudrate_list.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.baudrate_list.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.baudrate_list.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.baudrate_list.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.baudrate_list.addItem(item)
        self.gridLayout.addWidget(self.baudrate_list, 4, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.searchparamtxt = QtGui.QLabel(self.framesearch)
        self.searchparamtxt.setObjectName(_fromUtf8("searchparamtxt"))
        self.horizontalLayout_8.addWidget(self.searchparamtxt)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.framesearch, 0, 0, 1, 1)
        self.framelist = QtGui.QFrame(self.centralwidget)
        self.framelist.setFrameShape(QtGui.QFrame.NoFrame)
        self.framelist.setFrameShadow(QtGui.QFrame.Raised)
        self.framelist.setObjectName(_fromUtf8("framelist"))
        self.gridLayout_2 = QtGui.QGridLayout(self.framelist)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.framelist)
        self.label_6.setEnabled(True)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.table_found = QtGui.QTableWidget(self.framelist)
        self.table_found.setMaximumSize(QtCore.QSize(302, 16777215))
        self.table_found.setObjectName(_fromUtf8("table_found"))
        self.table_found.setColumnCount(3)
        self.table_found.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_found.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_found.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_found.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.table_found, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.framelist, 0, 1, 1, 1)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.frameconfig = QtGui.QFrame(self.centralwidget)
        self.frameconfig.setMaximumSize(QtCore.QSize(273, 523))
        self.frameconfig.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameconfig.setFrameShadow(QtGui.QFrame.Raised)
        self.frameconfig.setObjectName(_fromUtf8("frameconfig"))
        self.gridLayout_7 = QtGui.QGridLayout(self.frameconfig)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.torquemaxtxt = QtGui.QLabel(self.frameconfig)
        self.torquemaxtxt.setObjectName(_fromUtf8("torquemaxtxt"))
        self.horizontalLayout_2.addWidget(self.torquemaxtxt)
        self.torque_slider = QtGui.QSlider(self.frameconfig)
        self.torque_slider.setMinimum(1)
        self.torque_slider.setMaximum(100)
        self.torque_slider.setProperty("value", 100)
        self.torque_slider.setTracking(True)
        self.torque_slider.setOrientation(QtCore.Qt.Horizontal)
        self.torque_slider.setObjectName(_fromUtf8("torque_slider"))
        self.horizontalLayout_2.addWidget(self.torque_slider)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.torque_spin = QtGui.QSpinBox(self.frameconfig)
        self.torque_spin.setMinimum(1)
        self.torque_spin.setMaximum(100)
        self.torque_spin.setProperty("value", 100)
        self.torque_spin.setObjectName(_fromUtf8("torque_spin"))
        self.horizontalLayout_4.addWidget(self.torque_spin)
        self.label = QtGui.QLabel(self.frameconfig)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.reverse_mode = QtGui.QCheckBox(self.frameconfig)
        self.reverse_mode.setEnabled(False)
        self.reverse_mode.setObjectName(_fromUtf8("reverse_mode"))
        self.horizontalLayout_7.addWidget(self.reverse_mode)
        self.slave_mode = QtGui.QCheckBox(self.frameconfig)
        self.slave_mode.setEnabled(False)
        self.slave_mode.setObjectName(_fromUtf8("slave_mode"))
        self.horizontalLayout_7.addWidget(self.slave_mode)
        self.gridLayout_7.addLayout(self.horizontalLayout_7, 8, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.frameconfig)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.servoidtxt = QtGui.QLabel(self.frameconfig)
        self.servoidtxt.setObjectName(_fromUtf8("servoidtxt"))
        self.verticalLayout.addWidget(self.servoidtxt)
        self.servo_id = QtGui.QSpinBox(self.frameconfig)
        self.servo_id.setAccelerated(True)
        self.servo_id.setMinimum(1)
        self.servo_id.setMaximum(252)
        self.servo_id.setObjectName(_fromUtf8("servo_id"))
        self.verticalLayout.addWidget(self.servo_id)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.factory_reset_box = QtGui.QCheckBox(self.frameconfig)
        self.factory_reset_box.setObjectName(_fromUtf8("factory_reset_box"))
        self.gridLayout_3.addWidget(self.factory_reset_box, 1, 0, 1, 2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.newidtxt = QtGui.QLabel(self.frameconfig)
        self.newidtxt.setObjectName(_fromUtf8("newidtxt"))
        self.verticalLayout_3.addWidget(self.newidtxt)
        self.new_id = QtGui.QSpinBox(self.frameconfig)
        self.new_id.setAccelerated(True)
        self.new_id.setMinimum(1)
        self.new_id.setMaximum(252)
        self.new_id.setObjectName(_fromUtf8("new_id"))
        self.verticalLayout_3.addWidget(self.new_id)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.newbaud = QtGui.QLabel(self.frameconfig)
        self.newbaud.setObjectName(_fromUtf8("newbaud"))
        self.verticalLayout_4.addWidget(self.newbaud)
        self.new_baudlist = QtGui.QComboBox(self.frameconfig)
        self.new_baudlist.setObjectName(_fromUtf8("new_baudlist"))
        self.new_baudlist.addItem(_fromUtf8(""))
        self.new_baudlist.addItem(_fromUtf8(""))
        self.new_baudlist.addItem(_fromUtf8(""))
        self.new_baudlist.addItem(_fromUtf8(""))
        self.new_baudlist.addItem(_fromUtf8(""))
        self.new_baudlist.addItem(_fromUtf8(""))
        self.new_baudlist.addItem(_fromUtf8(""))
        self.new_baudlist.addItem(_fromUtf8(""))
        self.new_baudlist.addItem(_fromUtf8(""))
        self.verticalLayout_4.addWidget(self.new_baudlist)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 2, 2, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.servobaudrate = QtGui.QLabel(self.frameconfig)
        self.servobaudrate.setObjectName(_fromUtf8("servobaudrate"))
        self.verticalLayout_2.addWidget(self.servobaudrate)
        self.servo_baudlist = QtGui.QComboBox(self.frameconfig)
        self.servo_baudlist.setObjectName(_fromUtf8("servo_baudlist"))
        self.servo_baudlist.addItem(_fromUtf8(""))
        self.servo_baudlist.addItem(_fromUtf8(""))
        self.servo_baudlist.addItem(_fromUtf8(""))
        self.servo_baudlist.addItem(_fromUtf8(""))
        self.servo_baudlist.addItem(_fromUtf8(""))
        self.servo_baudlist.addItem(_fromUtf8(""))
        self.servo_baudlist.addItem(_fromUtf8(""))
        self.servo_baudlist.addItem(_fromUtf8(""))
        self.servo_baudlist.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.servo_baudlist)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.update_memory = QtGui.QPushButton(self.frameconfig)
        self.update_memory.setMaximumSize(QtCore.QSize(1920, 1080))
        self.update_memory.setStyleSheet(_fromUtf8("background-image: url(:/updateeprombut.jpg);"))
        self.update_memory.setFlat(False)
        self.update_memory.setObjectName(_fromUtf8("update_memory"))
        self.gridLayout_7.addWidget(self.update_memory, 9, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_16 = QtGui.QLabel(self.frameconfig)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_5.addWidget(self.label_16, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.wheel_mode = QtGui.QCheckBox(self.frameconfig)
        self.wheel_mode.setStyleSheet(_fromUtf8("background-image: url(:/background.jpg);"))
        self.wheel_mode.setObjectName(_fromUtf8("wheel_mode"))
        self.horizontalLayout_6.addWidget(self.wheel_mode)
        self.joint_mode = QtGui.QCheckBox(self.frameconfig)
        self.joint_mode.setAutoFillBackground(False)
        self.joint_mode.setCheckable(True)
        self.joint_mode.setTristate(False)
        self.joint_mode.setObjectName(_fromUtf8("joint_mode"))
        self.horizontalLayout_6.addWidget(self.joint_mode)
        self.multiturn_mode = QtGui.QCheckBox(self.frameconfig)
        self.multiturn_mode.setEnabled(False)
        self.multiturn_mode.setObjectName(_fromUtf8("multiturn_mode"))
        self.horizontalLayout_6.addWidget(self.multiturn_mode)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_13 = QtGui.QLabel(self.frameconfig)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_6.addWidget(self.label_13)
        self.cw_anglelimit = QtGui.QSpinBox(self.frameconfig)
        self.cw_anglelimit.setEnabled(False)
        self.cw_anglelimit.setFrame(True)
        self.cw_anglelimit.setAccelerated(True)
        self.cw_anglelimit.setKeyboardTracking(True)
        self.cw_anglelimit.setSuffix(_fromUtf8(""))
        self.cw_anglelimit.setMaximum(4095)
        self.cw_anglelimit.setObjectName(_fromUtf8("cw_anglelimit"))
        self.verticalLayout_6.addWidget(self.cw_anglelimit)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_14 = QtGui.QLabel(self.frameconfig)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_5.addWidget(self.label_14)
        self.ccw_anglelimit = QtGui.QSpinBox(self.frameconfig)
        self.ccw_anglelimit.setEnabled(False)
        self.ccw_anglelimit.setAccelerated(True)
        self.ccw_anglelimit.setMaximum(4095)
        self.ccw_anglelimit.setObjectName(_fromUtf8("ccw_anglelimit"))
        self.verticalLayout_5.addWidget(self.ccw_anglelimit)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 6, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frameconfig)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_7.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.frameconfig)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_8 = QtGui.QLabel(self.frameconfig)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.frameconfig)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.d_gain = QtGui.QSpinBox(self.frameconfig)
        self.d_gain.setAccelerated(True)
        self.d_gain.setMaximum(254)
        self.d_gain.setObjectName(_fromUtf8("d_gain"))
        self.horizontalLayout_9.addWidget(self.d_gain)
        self.i_gain = QtGui.QSpinBox(self.frameconfig)
        self.i_gain.setAccelerated(True)
        self.i_gain.setMaximum(254)
        self.i_gain.setObjectName(_fromUtf8("i_gain"))
        self.horizontalLayout_9.addWidget(self.i_gain)
        self.p_gain = QtGui.QSpinBox(self.frameconfig)
        self.p_gain.setAccelerated(True)
        self.p_gain.setMaximum(254)
        self.p_gain.setProperty("value", 32)
        self.p_gain.setObjectName(_fromUtf8("p_gain"))
        self.horizontalLayout_9.addWidget(self.p_gain)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.gridLayout_7.addLayout(self.verticalLayout_8, 7, 0, 1, 1)
        self.model_list = QtGui.QComboBox(self.frameconfig)
        self.model_list.setObjectName(_fromUtf8("model_list"))
        self.model_list.addItem(_fromUtf8(""))
        self.model_list.addItem(_fromUtf8(""))
        self.model_list.addItem(_fromUtf8(""))
        self.model_list.addItem(_fromUtf8(""))
        self.model_list.addItem(_fromUtf8(""))
        self.model_list.addItem(_fromUtf8(""))
        self.model_list.addItem(_fromUtf8(""))
        self.model_list.addItem(_fromUtf8(""))
        self.model_list.addItem(_fromUtf8(""))
        self.model_list.addItem(_fromUtf8(""))
        self.model_list.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.model_list, 2, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.frameconfig)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.gridLayout_6.addLayout(self.verticalLayout_7, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.baudrate_list.setCurrentRow(-1)
        QtCore.QObject.connect(self.torque_slider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.torque_spin.setValue)
        QtCore.QObject.connect(self.torque_spin, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.torque_slider.setValue)
        QtCore.QObject.connect(self.joint_mode, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.ccw_anglelimit.setEnabled)
        QtCore.QObject.connect(self.joint_mode, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cw_anglelimit.setEnabled)
        QtCore.QObject.connect(self.joint_mode, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.wheel_mode.setDisabled)
        QtCore.QObject.connect(self.wheel_mode, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.joint_mode.setDisabled)
        QtCore.QObject.connect(self.multiturn_mode, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.joint_mode.setDisabled)
        QtCore.QObject.connect(self.multiturn_mode, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.wheel_mode.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.multiturn_mode, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.joint_mode.setDisabled)

        #Everytime the model list current index changes, activated the enable_checkboxes method
        self.model_list.currentIndexChanged.connect(self.enable_checkboxes)
        #When multiturn mode is selected, activate uncheck_modes method
        self.multiturn_mode.clicked.connect(self.uncheck_modes)
        #Defines the Angle values when the mode is selected
        self.multiturn_mode.stateChanged.connect(self.define_angle_limit)
        self.wheel_mode.stateChanged.connect(self.define_angle_limit)
        self.joint_mode.stateChanged.connect(self.define_angle_limit)
        #Changes the cw angle limit and ccw angle limit according to the user input
        self.cw_anglelimit.valueChanged.connect(self.define_angle_limit)
        self.ccw_anglelimit.valueChanged.connect(self.define_angle_limit)
        #Saves the selected baudrates in a vector
        self.baudrate_list.itemClicked.connect(self.baudrates_to_search)
        #Connects search button to search method
        self.scan_btn.clicked.connect(self.network_search)
        #Connects the update memory button to configure method
        self.update_memory.clicked.connect(self.configure_confirmation)
        #Port changing
        self.port_combox.currentIndexChanged.connect(self.port_change)

    def enable_checkboxes(self):
        multiturn_servos_index = [7,8,9,10]
        reverse_slave_index = [10]

        if self.model_list.currentIndex() in multiturn_servos_index:
            self.multiturn_mode.setEnabled(True)
        else:
            self.multiturn_mode.setEnabled(False)

        if self.model_list.currentIndex() in reverse_slave_index:
            self.reverse_mode.setEnabled(True)
            self.slave_mode.setEnabled(True)
        else:
            self.reverse_mode.setEnabled(False)
            self.slave_mode.setEnabled(False)

    def uncheck_modes(self):
        """Uncheck wheel and joint mode checkbox"""
        self.wheel_mode.setCheckState(False)
        self.joint_mode.setCheckState(False)

    def define_angle_limit(self):
        """Sets the angle limits based on the mode selected"""
        #If wheel mode is selected set limits as 0
        if self.wheel_mode.checkState() == 2:
            self.cw_anglelimit.setValue(0)
            self.ccw_anglelimit.setValue(0)
        #if JOINT mode is selected, set limits as 4095
        elif self.joint_mode.checkState() == 2:
            self.cw_anglelimit.setValue(0)
            self.ccw_anglelimit.setValue(4095)
        #if multiturn mode is selected, set limits as 4095
        elif self.multiturn_mode.checkState() == 2:
            self.cw_anglelimit.setValue(4095)
            self.ccw_anglelimit.setValue(4095)

    def table_organize(self,found_servos):
        """Organizes the Found servos table with the search result"""
        #sets the number of rows
        self.table_found.setRowCount(len(found_servos))
        #Loop through the list and set the itens
        for i in found_servos:
            current_row = found_servos.index(i)
            #Creates the items
            id_item = QtGui.QTableWidgetItem(str(i.id))
            baudrate_item = QtGui.QTableWidgetItem(str(i.baudrate))
            model = mixcell.model_num[i.model]
            model_item =  QtGui.QTableWidgetItem(model)
            #Sets cells items
            self.table_found.setItem(current_row,0,id_item)
            self.table_found.setItem(current_row,1,model_item)
            self.table_found.setItem(current_row,2,baudrate_item)

    def baudrates_to_search(self):
        """Organizes the list with all the baudrates that will be used to search"""
    #Clear the list
        self.baudrates_search_list = []
        #Loops through the list and saves checked values
        for i in range(self.baudrate_list.count()):
            if self.baudrate_list.item(i).checkState() == QtCore.Qt.Checked:
                value = int(self.baudrate_list.item(i).text())
                self.baudrates_search_list.append(value)

    def network_search(self):
        """Search in the network for servos in the selected baudrates and in the ID range"""
        id_min = self.id_search_min.value()
        id_max = self.id_search_max.value()
        search_result = mixcell.search(id_min,id_max,self.baudrates_search_list)
        if search_result == mixcell.PORT_ERROR:
            self.port_error_message()
        elif search_result == mixcell.BAUDRATE_ERROR:
            self.baudrate_error_message()
        elif len(search_result) == 0:
            self.no_servos_found_message()
        else:
            self.table_organize(search_result)

    def port_error_message(self):
        """Displays the Port error message"""
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setText("Error while opening the port")
        msg.setWindowTitle("Port Error")
        msg.exec_()

    def hardware_comm_error_message(self):
        """Displays the hardware communication error message"""
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setText("Communication Hardware error!")
        msg.setWindowTitle("Hardware Comm error")
        msg.exec_()

    def comm_error_message(self):
        """Displays te communication error message"""
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setText("Communication error")
        msg.setWindowTitle("Comm Error")
        msg.exec_()

    def baudrate_error_message(self):
        """Displays the baudrate error message"""
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setText("Error while changing baudrate" )
        msg.setWindowTitle("Baudrate error")
        msg.exec_()

    def no_servos_found_message(self):
        """Displays the No servos were found on your network message"""
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.setText("No servos were found on your network, check your search parameters" )
        msg.setWindowTitle("Nothing found")
        msg.exec_()

    def configure_confirmation(self):
       """Displays the configure confirmation message"""
       msg = QtGui.QMessageBox()
       msg.setIcon(QtGui.QMessageBox.Question)
       msg.setText("Update memory?")
       msg.setWindowTitle("Confirmation")
       msg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
       rev = msg.exec_()
       if rev == QtGui.QMessageBox.Yes:
           self.configure()
       else:
           pass

    def configure(self):
        """Configures the servo as the parameters on the interface"""
        #User input
        id = self.servo_id.value()
        baudrate = int(self.servo_baudlist.currentText())

        #Checks if factory reset is marked
        if self.factory_reset_box.checkState() == 2:
            mixcell.factory_reset(id,baudrate)
        else:
            #Id to be configured
            new_id = self.new_id.value()

            #Sets ID
            id_change_result = mixcell.set_id(id, new_id,baudrate)
            if id_change_result == mixcell.PORT_ERROR:
                self.port_error_message()
            elif id_change_result == mixcell.BAUDRATE_ERROR:
                self.baudrate_error_message()
            else:
                id = new_id

            #Baudrate to be configured
            new_baudrate = int(self.new_baudlist.currentText())
            baudrate_change_result = mixcell.set_baudrate(id,new_baudrate,baudrate)
            if baudrate_change_result == mixcell.PORT_ERROR:
                self.port_error_message()
            elif baudrate_change_result == mixcell.BAUDRATE_ERROR:
                self.baudrate_error_message()
            if baudrate_change_result == mixcell.HARDWARE_COMM_ERROR:
                self.hardware_comm_error_message()
            elif baudrate_change_result == mixcell.COMM_ERROR:
                self.comm_error_message()
            else:
                baudrate = new_baudrate

            #Cw angle limit to be configured
            cw_angle_limit = self.cw_anglelimit.value()
            #CCW angle limit to be configured
            ccw_angle_limit = self.ccw_anglelimit.value()

            angle_limit_result = mixcell.set_angle_limit(id,cw_angle_limit,ccw_angle_limit,baudrate)
            if angle_limit_result == mixcell.PORT_ERROR:
                self.port_error_message()
            elif angle_limit_result == mixcell.BAUDRATE_ERROR:
                self.baudrate_error_message()
            elif angle_limit_result == mixcell.HARDWARE_COMM_ERROR:
                self.hardware_comm_error_message()
            elif angle_limit_result == mixcell.COMM_ERROR:
                self.comm_error_message

            #Torque value
            torque_value = self.torque_spin.value()
            torque_value_result = mixcell.set_torque_max(id,torque_value,baudrate)
            if torque_value_result == mixcell.PORT_ERROR:
                self.port_error_message()
            elif torque_value_result == mixcell.BAUDRATE_ERROR:
                self.baudrate_error_message()
            elif torque_value_result == mixcell.HARDWARE_COMM_ERROR:
                self.hardware_comm_error_message()
            elif torque_value_result == mixcell.COMM_ERROR:
                self.comm_error_message

            #D gain to be configured
            d_gain = self.d_gain.value()
            #I gain to be configured
            i_gain = self.i_gain.value()
            #P gain to be configured
            p_gain = self.p_gain.value()
            pid_gain_result = mixcell.set_pid_gain(id,d_gain,i_gain,p_gain,baudrate)
            if pid_gain_result == mixcell.PORT_ERROR:
                self.port_error_message()
            elif pid_gain_result == mixcell.BAUDRATE_ERROR:
                self.baudrate_error_message()
            elif pid_gain_result == mixcell.HARDWARE_COMM_ERROR:
                self.hardware_comm_error_message()
            elif pid_gain_result == mixcell.COMM_ERROR:
                self.comm_error_message

            if self.model_list.currentIndex() == 10:
                #Reverse mode checkbox state
                reverse_mode_enable = self.reverse_mode.checkState()
                #Slave mode checkbox state
                slave_mode_enable = self.slave_mode.checkState()
                reverse_slave_result =mixcell.reverse_slave(id,reverse_mode_enable,slave_mode_enable,baudrate)
                if reverse_slave_result == mixcell.PORT_ERROR:
                    self.port_error_message()
                elif reverse_slave_result == mixcell.BAUDRATE_ERROR:
                    self.baudrate_error_message()
                elif reverse_slave_result == mixcell.HARDWARE_COMM_ERROR:
                    self.hardware_comm_error_message()
                elif reverse_slave_result == mixcell.COMM_ERROR:
                    self.comm_error_message

            print("Operation complete!")

    def port_change(self):
        """Changes the current port based on the one selected in the interface"""
        port = str(self.port_combox.currentText())
        devicename = port.encode('-utf8')
        mixcell.DEVICENAME = devicename

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Mixcell", "Mixcell", None))
        self.label_4.setText(_translate("MainWindow", "Min. ID", None))
        self.label_5.setText(_translate("MainWindow", "Max. ID", None))
        self.portttxt.setText(_translate("MainWindow", "PORTS", None))
        self.port_combox.setItemText(0, _translate("MainWindow", "/dev/ttyUSB0", None))
        self.port_combox.setItemText(1, _translate("MainWindow", "/dev/ttyUSB1", None))
        self.port_combox.setItemText(2, _translate("MainWindow", "/dev/ttyUSB2", None))
        self.port_combox.setItemText(3, _translate("MainWindow", "/dev/ttyUSB3", None))
        self.BAUDRATEtxt.setText(_translate("MainWindow", "BAUDRATES", None))
        self.scan_btn.setText(_translate("MainWindow", "SCAN", None))
        self.baudrate_list.setSortingEnabled(False)
        __sortingEnabled = self.baudrate_list.isSortingEnabled()
        self.baudrate_list.setSortingEnabled(False)
        item = self.baudrate_list.item(0)
        item.setText(_translate("MainWindow", "1000000", None))
        item = self.baudrate_list.item(1)
        item.setText(_translate("MainWindow", "500000", None))
        item = self.baudrate_list.item(2)
        item.setText(_translate("MainWindow", "400000", None))
        item = self.baudrate_list.item(3)
        item.setText(_translate("MainWindow", "250000", None))
        item = self.baudrate_list.item(4)
        item.setText(_translate("MainWindow", "200000", None))
        item = self.baudrate_list.item(5)
        item.setText(_translate("MainWindow", "115200", None))
        item = self.baudrate_list.item(6)
        item.setText(_translate("MainWindow", "57600", None))
        item = self.baudrate_list.item(7)
        item.setText(_translate("MainWindow", "19200", None))
        item = self.baudrate_list.item(8)
        item.setText(_translate("MainWindow", "9600", None))
        self.baudrate_list.setSortingEnabled(__sortingEnabled)
        self.searchparamtxt.setText(_translate("MainWindow", "SEARCH PARAMETERS", None))
        self.label_6.setText(_translate("MainWindow", "Motors Found", None))
        item = self.table_found.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id", None))
        item = self.table_found.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Model", None))
        item = self.table_found.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Baudrate", None))
        self.torquemaxtxt.setText(_translate("MainWindow", "Torque Max", None))
        self.label.setText(_translate("MainWindow", "%", None))
        self.reverse_mode.setText(_translate("MainWindow", "Reverse Mode", None))
        self.slave_mode.setText(_translate("MainWindow", "Slave Mode", None))
        self.label_7.setText(_translate("MainWindow", "Configuration Parameters", None))
        self.servoidtxt.setText(_translate("MainWindow", "Servo ID", None))
        self.factory_reset_box.setText(_translate("MainWindow", "Factory Reset", None))
        self.newidtxt.setText(_translate("MainWindow", "New ID", None))
        self.newbaud.setText(_translate("MainWindow", "New Baudrate", None))
        self.new_baudlist.setItemText(0, _translate("MainWindow", "1000000", None))
        self.new_baudlist.setItemText(1, _translate("MainWindow", "500000", None))
        self.new_baudlist.setItemText(2, _translate("MainWindow", "400000", None))
        self.new_baudlist.setItemText(3, _translate("MainWindow", "250000", None))
        self.new_baudlist.setItemText(4, _translate("MainWindow", "200000", None))
        self.new_baudlist.setItemText(5, _translate("MainWindow", "11520", None))
        self.new_baudlist.setItemText(6, _translate("MainWindow", "57600", None))
        self.new_baudlist.setItemText(7, _translate("MainWindow", "19200", None))
        self.new_baudlist.setItemText(8, _translate("MainWindow", "9600", None))
        self.servobaudrate.setText(_translate("MainWindow", "Servo Baudrate", None))
        self.servo_baudlist.setItemText(0, _translate("MainWindow", "1000000", None))
        self.servo_baudlist.setItemText(1, _translate("MainWindow", "500000", None))
        self.servo_baudlist.setItemText(2, _translate("MainWindow", "400000", None))
        self.servo_baudlist.setItemText(3, _translate("MainWindow", "250000", None))
        self.servo_baudlist.setItemText(4, _translate("MainWindow", "200000", None))
        self.servo_baudlist.setItemText(5, _translate("MainWindow", "11520", None))
        self.servo_baudlist.setItemText(6, _translate("MainWindow", "57600", None))
        self.servo_baudlist.setItemText(7, _translate("MainWindow", "19200", None))
        self.servo_baudlist.setItemText(8, _translate("MainWindow", "9600", None))
        self.update_memory.setText(_translate("MainWindow", "UPDATE MEMORY", None))
        self.label_16.setText(_translate("MainWindow", "Mode set", None))
        self.wheel_mode.setText(_translate("MainWindow", "Wheel", None))
        self.joint_mode.setText(_translate("MainWindow", "Joint", None))
        self.multiturn_mode.setText(_translate("MainWindow", "Multi Turn", None))
        self.label_13.setText(_translate("MainWindow", "CW ANGLE LIMIT", None))
        self.label_14.setText(_translate("MainWindow", "CCW ANGLE LIMIT", None))
        self.label_2.setText(_translate("MainWindow", "Model", None))
        self.label_3.setText(_translate("MainWindow", "D Gain", None))
        self.label_8.setText(_translate("MainWindow", "I Gain", None))
        self.label_9.setText(_translate("MainWindow", "P Gain", None))
        self.model_list.setItemText(0, _translate("MainWindow", "AX-12W", None))
        self.model_list.setItemText(1, _translate("MainWindow", "AX-12A", None))
        self.model_list.setItemText(2, _translate("MainWindow", "AX-18", None))
        self.model_list.setItemText(3, _translate("MainWindow", "EX-106+ ", None))
        self.model_list.setItemText(4, _translate("MainWindow", "RX-24F ", None))
        self.model_list.setItemText(5, _translate("MainWindow", "RX-28 ", None))
        self.model_list.setItemText(6, _translate("MainWindow", "RX-64", None))
        self.model_list.setItemText(7, _translate("MainWindow", "MX-12W ", None))
        self.model_list.setItemText(8, _translate("MainWindow", "MX-28", None))
        self.model_list.setItemText(9, _translate("MainWindow", "MX-64", None))
        self.model_list.setItemText(10, _translate("MainWindow", "MX-106", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
