from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 450)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.status_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.verticalLayout.addWidget(self.status_label)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                btn = QtWidgets.QPushButton(Form)
                btn.setMinimumSize(QtCore.QSize(100, 100))
                font = QtGui.QFont()
                font.setPointSize(20)
                btn.setFont(font)
                btn.setObjectName(f"button_{row}_{col}")
                self.gridLayout.addWidget(btn, row, col)
                button_row.append(btn)
            self.buttons.append(button_row)

        self.verticalLayout.addLayout(self.gridLayout)

        self.winner_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.winner_label.setFont(font)
        self.winner_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.winner_label.setText("")
        self.winner_label.setObjectName("winner_label")
        self.verticalLayout.addWidget(self.winner_label)

        self.restart_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.restart_button.setFont(font)
        self.restart_button.setObjectName("restart_button")
        self.verticalLayout.addWidget(self.restart_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tic Tac Toe"))
        self.status_label.setText(_translate("Form", "Player X's turn"))
        self.restart_button.setText(_translate("Form", "Restart"))

