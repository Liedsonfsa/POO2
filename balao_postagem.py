# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'balao_postagem.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 100)
        MainWindow.setMinimumSize(QtCore.QSize(300, 100))
        MainWindow.setMaximumSize(QtCore.QSize(300, 100))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(300, 100))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tela_perfil = QtWidgets.QFrame(self.centralwidget)
        self.tela_perfil.setStyleSheet("background-color:rgb(185, 252, 201);\n"
"")
        self.tela_perfil.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tela_perfil.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tela_perfil.setObjectName("tela_perfil")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tela_perfil)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_nome_dono = QtWidgets.QFrame(self.tela_perfil)
        self.frame_nome_dono.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_nome_dono.setMaximumSize(QtCore.QSize(16777215, 23))
        self.frame_nome_dono.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_nome_dono.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_nome_dono.setObjectName("frame_nome_dono")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_nome_dono)
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nome_dono = QtWidgets.QTextBrowser(self.frame_nome_dono)
        self.nome_dono.setMaximumSize(QtCore.QSize(16777215, 23))
        self.nome_dono.setObjectName("nome_dono")
        self.horizontalLayout.addWidget(self.nome_dono)
        self.data_postagem = QtWidgets.QTextBrowser(self.frame_nome_dono)
        self.data_postagem.setMaximumSize(QtCore.QSize(125, 16777215))
        self.data_postagem.setObjectName("data_postagem")
        self.horizontalLayout.addWidget(self.data_postagem)
        self.verticalLayout_2.addWidget(self.frame_nome_dono)
        self.frame_mensagem = QtWidgets.QFrame(self.tela_perfil)
        self.frame_mensagem.setMinimumSize(QtCore.QSize(0, 48))
        self.frame_mensagem.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_mensagem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mensagem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mensagem.setObjectName("frame_mensagem")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_mensagem)
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.mensagem_postagem = QtWidgets.QTextBrowser(self.frame_mensagem)
        self.mensagem_postagem.setObjectName("mensagem_postagem")
        self.verticalLayout_4.addWidget(self.mensagem_postagem)
        self.verticalLayout_2.addWidget(self.frame_mensagem)
        self.verticalLayout.addWidget(self.tela_perfil)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
# import icones_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
