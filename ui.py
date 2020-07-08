"""
-*- coding: utf-8 -*-
Form implementation generated from reading ui file 'epictictactoe.ui'
Created by: PyQt5 UI code generator 5.9.2
WARNING! All changes made in this file will be lost!
"""

from PyQt5 import QtCore, QtGui, QtWidgets
TURN = 0
pButtons = []
print('X turn to play')

def display(button, label, text):
    """"Displays messages on label"""
    print(button.text() + text)
    label.setText(button.text() + text)

def replay(label):
    """Starts new game"""
    global TURN
    TURN = 0
    for i in range(9):
        pButtons[i].setText('')
    label.setText('X turn to play')

def wincheck(label):
    """Checks for win/draw"""
    win = False
    if (pButtons[0].text() == pButtons[1].text() == pButtons[2].text()) \
        and (pButtons[0].text() != ''):
        display(pButtons[0], label, ' wins!')
        win = True
    elif (pButtons[3].text() == pButtons[4].text() == pButtons[5].text()) \
        and (pButtons[3].text() != ''):
        display(pButtons[3], label, ' wins!')
        win = True
    elif (pButtons[6].text() == pButtons[7].text() == pButtons[8].text()) \
        and (pButtons[6].text() != ''):
        display(pButtons[6], label, ' wins!')
        win = True
    elif (pButtons[0].text() == pButtons[3].text() == pButtons[6].text()) \
        and (pButtons[0].text() != ''):
        display(pButtons[0], label, ' wins!')
        win = True
    elif (pButtons[1].text() == pButtons[4].text() == pButtons[7].text()) \
        and (pButtons[1].text() != ''):
        display(pButtons[1], label, ' wins!')
        win = True
    elif (pButtons[2].text() == pButtons[5].text() == pButtons[8].text()) \
        and (pButtons[2].text() != ''):
        display(pButtons[2], label, ' wins!')
        win = True
    elif (pButtons[0].text() == pButtons[4].text() == pButtons[8].text()) \
        and (pButtons[0].text() != ''):
        display(pButtons[0], label, ' wins!')
        win = True
    elif (pButtons[2].text() == pButtons[4].text() == pButtons[6].text()) \
        and (pButtons[2].text() != ''):
        display(pButtons[2], label, ' wins!')
        win = True
    elif TURN >= 9:
        print('Draw')
        label.setText('Draw')
        win = True
    return win

def turncheck(button, label):
    """Turn to play"""
    if not wincheck(label):
        if button.text() == 'X':
            print('O turn to play')
            label.setText('O turn to play')
        elif button.text() == 'O':
            print('X turn to play')
            label.setText('X turn to play')

def turn_num(button, label):
    """turn number"""
    global TURN
    if not wincheck(label):
        if button.text() == '':
            if TURN %2 == 0:
                button.setText('X')
            else:
                button.setText('O')
            TURN += 1
        turncheck(button, label)
    else:
        print('Please start a new game.')
        label.setText('Please start a new game.')

class UiMainWindow():
    """Main window gui"""
    def setup_ui(self, main_window):
        """Sets up the window"""
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(24)
        for i in range(9):
            push_button = QtWidgets.QPushButton(self.centralwidget)
            push_button.setGeometry(QtCore.QRect(160+i%3*140, 70+int(i/3)*130, 141, 131))
            push_button.setText("")
            push_button.setObjectName("push_button" + str(i))
            push_button.setFont(font)
            push_button.raise_()
            pButtons.append(push_button)

        self.push_button_10 = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_10.setGeometry(QtCore.QRect(320, 480, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_button_10.setFont(font)
        self.push_button_10.setObjectName("push_button_10")
        self.push_button_10.raise_()

        main_window.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-70, 10, 891, 61))
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.retranslate_ui(main_window)

        pButtons[0].clicked.connect(lambda: turn_num(pButtons[0], self.label))
        pButtons[1].clicked.connect(lambda: turn_num(pButtons[1], self.label))
        pButtons[2].clicked.connect(lambda: turn_num(pButtons[2], self.label))
        pButtons[3].clicked.connect(lambda: turn_num(pButtons[3], self.label))
        pButtons[4].clicked.connect(lambda: turn_num(pButtons[4], self.label))
        pButtons[5].clicked.connect(lambda: turn_num(pButtons[5], self.label))
        pButtons[6].clicked.connect(lambda: turn_num(pButtons[6], self.label))
        pButtons[7].clicked.connect(lambda: turn_num(pButtons[7], self.label))
        pButtons[8].clicked.connect(lambda: turn_num(pButtons[8], self.label))

        self.push_button_10.clicked.connect(lambda: replay(self.label))

        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        """Qt Designer code"""
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Tic-Tac-Toe"))
        self.label.setText(_translate("main_window", "X turn to play"))
        self.push_button_10.setText(_translate("main_window", "Replay"))
