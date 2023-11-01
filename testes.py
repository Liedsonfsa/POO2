# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_Perfil.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Perfil(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 530)
        MainWindow.setMinimumSize(QtCore.QSize(300, 530))
        MainWindow.setMaximumSize(QtCore.QSize(300, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tela_perfil = QtWidgets.QFrame(self.centralwidget)
        self.tela_perfil.setStyleSheet("background-color: rgb(170, 232, 185);\n"
"")
        self.tela_perfil.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tela_perfil.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tela_perfil.setObjectName("tela_perfil")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tela_perfil)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.perfil_infos = QtWidgets.QFrame(self.tela_perfil)
        self.perfil_infos.setMaximumSize(QtCore.QSize(16777215, 80))
        self.perfil_infos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.perfil_infos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.perfil_infos.setObjectName("perfil_infos")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.perfil_infos)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.foto_perfil = QtWidgets.QFrame(self.perfil_infos)
        self.foto_perfil.setMaximumSize(QtCore.QSize(60, 16777215))
        self.foto_perfil.setStyleSheet("QFrame{\n"
"    \n"
"    image: url(:/icones/pato.jpg);\n"
"    \n"
"    border-radius : 100px;\n"
"    border: 3px solid rgb(54, 255, 32)\n"
"}")
        self.foto_perfil.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.foto_perfil.setFrameShadow(QtWidgets.QFrame.Plain)
        self.foto_perfil.setObjectName("foto_perfil")
        self.horizontalLayout_2.addWidget(self.foto_perfil)
        self.infos = QtWidgets.QFrame(self.perfil_infos)
        self.infos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.infos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infos.setObjectName("infos")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.infos)
        self.verticalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Nome = QtWidgets.QLabel(self.infos)
        self.Nome.setStyleSheet("font: 87 15pt \"Arial Black\";")
        self.Nome.setObjectName("Nome")
        self.verticalLayout_3.addWidget(self.Nome)
        self.Email = QtWidgets.QLabel(self.infos)
        self.Email.setObjectName("Email")
        self.verticalLayout_3.addWidget(self.Email)
        self.horizontalLayout_2.addWidget(self.infos)
        self.verticalLayout_2.addWidget(self.perfil_infos)
        self.tela_perfil_meio = QtWidgets.QFrame(self.tela_perfil)
        self.tela_perfil_meio.setMinimumSize(QtCore.QSize(0, 300))
        self.tela_perfil_meio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tela_perfil_meio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tela_perfil_meio.setObjectName("tela_perfil_meio")
        self.gridLayout = QtWidgets.QGridLayout(self.tela_perfil_meio)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2.addWidget(self.tela_perfil_meio)
        self.tela_perfil_baixo = QtWidgets.QFrame(self.tela_perfil)
        self.tela_perfil_baixo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.tela_perfil_baixo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tela_perfil_baixo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tela_perfil_baixo.setObjectName("tela_perfil_baixo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tela_perfil_baixo)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botao_conversas = QtWidgets.QPushButton(self.tela_perfil_baixo)
        self.botao_conversas.setMaximumSize(QtCore.QSize(150, 16777215))
        self.botao_conversas.setStyleSheet("QPushButton {\n"
"    border: 3px solid rgb(146, 232, 141);\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"    background-color:  rgb(146, 232, 141);\n"
"    color: rgb(0,0,0);\n"
"    \n"
"    font: 87 11pt \"Arial Black\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgb(95, 232, 71);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 255, 0);\n"
"}\n"
"")
        self.botao_conversas.setObjectName("botao_conversas")
        self.horizontalLayout.addWidget(self.botao_conversas)
        self.botao_inicio = QtWidgets.QPushButton(self.tela_perfil_baixo)
        self.botao_inicio.setMaximumSize(QtCore.QSize(150, 16777215))
        self.botao_inicio.setStyleSheet("QPushButton {\n"
"    border: 3px solid rgb(146, 232, 141);\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"    background-color:  rgb(146, 232, 141);\n"
"    color: rgb(0,0,0);\n"
"    \n"
"    font: 87 11pt \"Arial Black\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgb(95, 232, 71);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 255, 0);\n"
"}\n"
"")
        self.botao_inicio.setObjectName("botao_inicio")
        self.horizontalLayout.addWidget(self.botao_inicio)
        self.botao_sair = QtWidgets.QPushButton(self.tela_perfil_baixo)
        self.botao_sair.setMaximumSize(QtCore.QSize(150, 16777215))
        self.botao_sair.setStyleSheet("QPushButton {\n"
"    border: 3px solid rgb(146, 232, 141);\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"    background-color:  rgb(146, 232, 141);\n"
"    color: rgb(0,0,0);\n"
"    \n"
"    font: 87 11pt \"Arial Black\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgb(95, 232, 71);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 255, 0);\n"
"}\n"
"")
        self.botao_sair.setObjectName("botao_sair")
        self.horizontalLayout.addWidget(self.botao_sair)
        self.verticalLayout_2.addWidget(self.tela_perfil_baixo)
        self.verticalLayout.addWidget(self.tela_perfil)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Nome.setText(_translate("MainWindow", "Nome do Usuario"))
        self.Email.setText(_translate("MainWindow", "email_do_usuario@mail.com"))
        self.botao_conversas.setText(_translate("MainWindow", "Conversas"))
        self.botao_inicio.setText(_translate("MainWindow", "Inicio"))
        self.botao_sair.setText(_translate("MainWindow", "Sair"))
#import icones_rc
