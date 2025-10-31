from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:rgb(204, 186, 236);\n"
"")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 20, 950, 750))
        self.stackedWidget.setMinimumSize(QtCore.QSize(900, 700))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("background-color: rgb(233, 223, 245);\n"
"border-radius: 15px;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setStyleSheet("border-radius:15px;")
        self.login_page.setObjectName("login_page")
        self.login = QtWidgets.QWidget(self.login_page)
        self.login.setGeometry(QtCore.QRect(40, 40, 450, 670))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setMinimumSize(QtCore.QSize(450, 620))
        self.login.setStyleSheet("background-color: rgba(0, 0, 0, 40);\n"
"border-radius: 20px;")
        self.login.setObjectName("login")
        self.login_title = QtWidgets.QLabel(self.login)
        self.login_title.setGeometry(QtCore.QRect(150, 60, 145, 60))
        self.login_title.setMinimumSize(QtCore.QSize(145, 60))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.login_title.setFont(font)
        self.login_title.setAutoFillBackground(False)
        self.login_title.setStyleSheet("color:rgba(255, 255, 255, 210);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.login_title.setObjectName("login_title")
        self.username_1 = QtWidgets.QLineEdit(self.login)
        self.username_1.setGeometry(QtCore.QRect(44, 180, 351, 50))
        self.username_1.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_1.setFont(font)
        self.username_1.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-radius: none;\n"
"border-bottom: 2px solid rgba(200, 120, 200, 255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.username_1.setObjectName("username_1")
        self.password_1 = QtWidgets.QLineEdit(self.login)
        self.password_1.setGeometry(QtCore.QRect(44, 280, 351, 50))
        self.password_1.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_1.setFont(font)
        self.password_1.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-radius: none;\n"
"border-bottom: 2px solid rgba(200, 120, 200, 255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.password_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_1.setCursorPosition(0)
        self.password_1.setObjectName("password_1")
        self.login_button = QtWidgets.QPushButton(self.login)
        self.login_button.setGeometry(QtCore.QRect(69, 400, 301, 55))
        self.login_button.setMinimumSize(QtCore.QSize(290, 55))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("QPushButton {\n"
"    color:rgba(255, 255, 255, 200);\n"
"}\n"
"QPushButton {\n"
"    background-color:qlineargradient(spread:pad, x3:1, y2:1.926136, x2:2, y2:2.193, stop:0     rgba(180, 70, 180, 110), stop:1 rgba(255, 255, 0, 0));\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(180, 70, 180);\n"
"}")
        self.login_button.setObjectName("login_button")
        self.go_to_signup_page = QtWidgets.QPushButton(self.login)
        self.go_to_signup_page.setGeometry(QtCore.QRect(75, 490, 290, 25))
        self.go_to_signup_page.setMinimumSize(QtCore.QSize(290, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setUnderline(False)
        self.go_to_signup_page.setFont(font)
        self.go_to_signup_page.setStyleSheet("QPushButton {\n"
"    color:rgba(255, 255, 255, 140);\n"
"}\n"
"QPushButton {\n"
"    background-color: none\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgba(255, 255, 255, 200);\n"
"}")
        self.go_to_signup_page.setObjectName("go_to_signup_page")
        self.login_label = QtWidgets.QLabel(self.login)
        self.login_label.setGeometry(QtCore.QRect(50, 540, 340, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color:rgba(255, 255, 255, 100);\n"
"background-color:rgba(20, 20, 20, 3);\n"
"border-radius: 10px;\n"
"")
        self.login_label.setText("")
        self.login_label.setObjectName("login_label")
        self.google_auth = QtWidgets.QPushButton(self.login)
        self.google_auth.setGeometry(QtCore.QRect(185, 590, 70, 50))
        self.google_auth.setStyleSheet("QPushButton {\n"
"    background-color:rgba(20, 20, 20, 30);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgba(20, 20, 20, 35);\n"
"}")
        self.google_auth.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/Google_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.google_auth.setIcon(icon1)
        self.google_auth.setIconSize(QtCore.QSize(40, 40))
        self.google_auth.setObjectName("google_auth")
        self.backpic_1 = QtWidgets.QLabel(self.login_page)
        self.backpic_1.setGeometry(QtCore.QRect(0, 0, 950, 750))
        self.backpic_1.setMinimumSize(QtCore.QSize(900, 700))
        self.backpic_1.setStyleSheet("border-image: url(:/images/login_signup.jpg);\n"
"border-radius: 15px;\n"
"border-image: url(:/images/images/login_signup.jpg);")
        self.backpic_1.setText("")
        self.backpic_1.setObjectName("backpic_1")
        self.backpic_1.raise_()
        self.login.raise_()
        self.stackedWidget.addWidget(self.login_page)
        self.signup_page = QtWidgets.QWidget()
        self.signup_page.setStyleSheet("border-radius:15px;")
        self.signup_page.setObjectName("signup_page")
        self.signup = QtWidgets.QWidget(self.signup_page)
        self.signup.setGeometry(QtCore.QRect(40, 40, 450, 670))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signup.sizePolicy().hasHeightForWidth())
        self.signup.setSizePolicy(sizePolicy)
        self.signup.setMinimumSize(QtCore.QSize(450, 620))
        self.signup.setStyleSheet("background-color: rgba(0, 0, 0, 40);\n"
"border-radius: 20px;")
        self.signup.setObjectName("signup")
        self.signup_title = QtWidgets.QLabel(self.signup)
        self.signup_title.setGeometry(QtCore.QRect(140, 65, 170, 70))
        self.signup_title.setMinimumSize(QtCore.QSize(170, 60))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.signup_title.setFont(font)
        self.signup_title.setStyleSheet("color:rgba(255, 255, 255, 210);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.signup_title.setObjectName("signup_title")
        self.email = QtWidgets.QLineEdit(self.signup)
        self.email.setGeometry(QtCore.QRect(45, 160, 361, 50))
        self.email.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-radius: none;\n"
"border-bottom: 2px solid rgba(200, 120, 200, 255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.email.setObjectName("email")
        self.username_2 = QtWidgets.QLineEdit(self.signup)
        self.username_2.setGeometry(QtCore.QRect(45, 250, 361, 50))
        self.username_2.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_2.setFont(font)
        self.username_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-radius: none;\n"
"border-bottom: 2px solid rgba(200, 120, 200, 255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.username_2.setObjectName("username_2")
        self.password_2 = QtWidgets.QLineEdit(self.signup)
        self.password_2.setGeometry(QtCore.QRect(45, 340, 361, 50))
        self.password_2.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_2.setFont(font)
        self.password_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-radius: none;\n"
"border-bottom: 2px solid rgba(200, 120, 200, 255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setObjectName("password_2")
        self.signup_button = QtWidgets.QPushButton(self.signup)
        self.signup_button.setGeometry(QtCore.QRect(80, 440, 290, 55))
        self.signup_button.setMinimumSize(QtCore.QSize(290, 55))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet("QPushButton {\n"
"    color:rgba(255, 255, 255, 200);\n"
"}\n"
"QPushButton {\n"
"    background-color:qlineargradient(spread:pad, x3:1, y2:1.926136, x2:2, y2:2.193, stop:0     rgba(180, 70, 180, 110), stop:1 rgba(255, 255, 0, 0));\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(180, 70, 180);\n"
"}")
        self.signup_button.setObjectName("signup_button")
        self.go_to_login_page = QtWidgets.QPushButton(self.signup)
        self.go_to_login_page.setGeometry(QtCore.QRect(129, 530, 191, 25))
        self.go_to_login_page.setMinimumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)
        self.go_to_login_page.setFont(font)
        self.go_to_login_page.setStyleSheet("QPushButton {\n"
"    color:rgba(255, 255, 255, 140);\n"
"}\n"
"QPushButton {\n"
"    background-color: none\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgba(255, 255, 255, 200);\n"
"}")
        self.go_to_login_page.setObjectName("go_to_login_page")
        self.signup_label = QtWidgets.QLabel(self.signup)
        self.signup_label.setGeometry(QtCore.QRect(49, 590, 351, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.signup_label.setFont(font)
        self.signup_label.setStyleSheet("color:rgba(255, 255, 255, 100);\n"
"background-color:rgba(20, 20, 20, 3);\n"
"border-radius: 10px;\n"
"")
        self.signup_label.setText("")
        self.signup_label.setObjectName("signup_label")
        self.signup_title.raise_()
        self.email.raise_()
        self.username_2.raise_()
        self.password_2.raise_()
        self.go_to_login_page.raise_()
        self.signup_button.raise_()
        self.signup_label.raise_()
        self.backpic_2 = QtWidgets.QLabel(self.signup_page)
        self.backpic_2.setGeometry(QtCore.QRect(0, 0, 950, 750))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backpic_2.sizePolicy().hasHeightForWidth())
        self.backpic_2.setSizePolicy(sizePolicy)
        self.backpic_2.setMinimumSize(QtCore.QSize(900, 700))
        self.backpic_2.setStyleSheet("border-image: url(:/images/images/login_signup.jpg);\n"
"border-radius: 15px;")
        self.backpic_2.setText("")
        self.backpic_2.setObjectName("backpic_2")
        self.backpic_2.raise_()
        self.signup.raise_()
        self.stackedWidget.addWidget(self.signup_page)
        self.main_page = QtWidgets.QWidget()
        self.main_page.setStyleSheet("border-radius:15px;")
        self.main_page.setObjectName("main_page")
        self.backpic_3 = QtWidgets.QLabel(self.main_page)
        self.backpic_3.setGeometry(QtCore.QRect(0, 0, 950, 750))
        self.backpic_3.setMinimumSize(QtCore.QSize(900, 700))
        self.backpic_3.setStyleSheet("border-image: url(:/images/images/main_back.jpg);\n"
"border-radius:15px;")
        self.backpic_3.setLineWidth(0)
        self.backpic_3.setText("")
        self.backpic_3.setObjectName("backpic_3")
        self.enter_answer = QtWidgets.QTextEdit(self.main_page)
        self.enter_answer.setGeometry(QtCore.QRect(370, 90, 290, 50))
        self.enter_answer.setMinimumSize(QtCore.QSize(280, 40))
        self.enter_answer.setMaximumSize(QtCore.QSize(370, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.enter_answer.setFont(font)
        self.enter_answer.setStyleSheet("background-color: rgba(233, 223, 245, 230);\n"
"border-radius: 15px;")
        self.enter_answer.setMarkdown("")
        self.enter_answer.setObjectName("enter_answer")
        self.flashcard_button = QtWidgets.QPushButton(self.main_page)
        self.flashcard_button.setGeometry(QtCore.QRect(60, 170, 200, 50))
        self.flashcard_button.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.flashcard_button.setFont(font)
        self.flashcard_button.setStyleSheet("QPushButton {\n"
"    color:rgb(83, 60, 98);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgb(152, 137, 235);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(139, 125, 218);\n"
"}")
        self.flashcard_button.setIconSize(QtCore.QSize(20, 20))
        self.flashcard_button.setObjectName("flashcard_button")
        self.go_back = QtWidgets.QPushButton(self.main_page)
        self.go_back.setGeometry(QtCore.QRect(10, 10, 70, 50))
        self.go_back.setMinimumSize(QtCore.QSize(70, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.go_back.setFont(font)
        self.go_back.setStyleSheet("QPushButton {\n"
"    color:rgb(57, 41, 67);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgba(144, 130, 222, 120);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgba(133, 120, 206, 120);\n"
"}")
        self.go_back.setIconSize(QtCore.QSize(20, 20))
        self.go_back.setObjectName("go_back")
        self.enter_question = QtWidgets.QTextEdit(self.main_page)
        self.enter_question.setGeometry(QtCore.QRect(60, 90, 290, 50))
        self.enter_question.setMinimumSize(QtCore.QSize(290, 40))
        self.enter_question.setMaximumSize(QtCore.QSize(370, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.enter_question.setFont(font)
        self.enter_question.setStyleSheet("background-color: rgba(233, 223, 245, 230);\n"
"border-radius: 15px;")
        self.enter_question.setMarkdown("")
        self.enter_question.setObjectName("enter_question")
        self.next_flashcard_button = QtWidgets.QPushButton(self.main_page)
        self.next_flashcard_button.setGeometry(QtCore.QRect(690, 340, 200, 50))
        self.next_flashcard_button.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.next_flashcard_button.setFont(font)
        self.next_flashcard_button.setStyleSheet("QPushButton {\n"
"    color:rgb(83, 60, 98);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgb(160, 144, 246);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(139, 125, 218);\n"
"}")
        self.next_flashcard_button.setIconSize(QtCore.QSize(20, 20))
        self.next_flashcard_button.setObjectName("next_flashcard_button")
        self.save_flashcard_button = QtWidgets.QPushButton(self.main_page)
        self.save_flashcard_button.setGeometry(QtCore.QRect(690, 400, 200, 50))
        self.save_flashcard_button.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_flashcard_button.setFont(font)
        self.save_flashcard_button.setStyleSheet("QPushButton {\n"
"    color:rgb(83, 60, 98);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgb(160, 144, 246);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(139, 125, 218);\n"
"}")
        self.save_flashcard_button.setIconSize(QtCore.QSize(20, 20))
        self.save_flashcard_button.setObjectName("save_flashcard_button")
        self.show_answer_button = QtWidgets.QPushButton(self.main_page)
        self.show_answer_button.setGeometry(QtCore.QRect(690, 280, 200, 50))
        self.show_answer_button.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.show_answer_button.setFont(font)
        self.show_answer_button.setStyleSheet("QPushButton {\n"
"    color:rgb(83, 60, 98);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgb(160, 144, 246);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(139, 125, 218);\n"
"}")
        self.show_answer_button.setIconSize(QtCore.QSize(20, 20))
        self.show_answer_button.setObjectName("show_answer_button")
        self.Flashcard_content = QtWidgets.QTextEdit(self.main_page)
        self.Flashcard_content.setGeometry(QtCore.QRect(50, 260, 590, 400))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Flashcard_content.setFont(font)
        self.Flashcard_content.setStyleSheet("QTextEdit {\n"
"    background-color: rgba(235, 235, 250, 130);\n"
"    border-radius: 20px;\n"
"    color: rgb(75, 54, 89);\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTextEdit::text {\n"
"    text-align: center;\n"
"}\n"
"")
        self.Flashcard_content.setReadOnly(True)
        self.Flashcard_content.setObjectName("Flashcard_content")
        self.go_to_Q_A = QtWidgets.QPushButton(self.main_page)
        self.go_to_Q_A.setGeometry(QtCore.QRect(690, 530, 200, 50))
        self.go_to_Q_A.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.go_to_Q_A.setFont(font)
        self.go_to_Q_A.setStyleSheet("QPushButton {\n"
"    color:rgb(83, 60, 98);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgb(193, 180, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(170, 159, 225);\n"
"}")
        self.go_to_Q_A.setIconSize(QtCore.QSize(20, 20))
        self.go_to_Q_A.setObjectName("go_to_Q_A")
        self.go_to_saved_flashcards = QtWidgets.QPushButton(self.main_page)
        self.go_to_saved_flashcards.setGeometry(QtCore.QRect(690, 590, 200, 50))
        self.go_to_saved_flashcards.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.go_to_saved_flashcards.setFont(font)
        self.go_to_saved_flashcards.setStyleSheet("QPushButton {\n"
"    color:rgb(83, 60, 98);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgb(193, 180, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(170, 159, 225);\n"
"}")
        self.go_to_saved_flashcards.setIconSize(QtCore.QSize(20, 20))
        self.go_to_saved_flashcards.setObjectName("go_to_saved_flashcards")
        self.stackedWidget.addWidget(self.main_page)
        self.saved_flashcards_page = QtWidgets.QWidget()
        self.saved_flashcards_page.setObjectName("saved_flashcards_page")
        self.backpic_5 = QtWidgets.QLabel(self.saved_flashcards_page)
        self.backpic_5.setGeometry(QtCore.QRect(0, 0, 950, 750))
        self.backpic_5.setMinimumSize(QtCore.QSize(900, 700))
        self.backpic_5.setStyleSheet("border-image: url(:/images/images/main_back.jpg);\n"
"border-radius:15px;")
        self.backpic_5.setText("")
        self.backpic_5.setObjectName("backpic_5")
        self.flashcard_list_widget = QtWidgets.QListWidget(self.saved_flashcards_page)
        self.flashcard_list_widget.setGeometry(QtCore.QRect(20, 100, 390, 600))
        self.flashcard_list_widget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.flashcard_list_widget.setFont(font)
        self.flashcard_list_widget.setStyleSheet("QListWidget::item {\n"
"    background-color: rgba(253, 147, 169, 50);\n"
"    text-align: left;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"    margin: 5px;\n"
"    border-radius: 5px;\n"
"    color: rgb(77, 62, 122);\n"
"}\n"
"QListWidget {\n"
"    background-color: rgba(233, 223, 245, 180);\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.flashcard_list_widget.setMidLineWidth(1)
        self.flashcard_list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.flashcard_list_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.flashcard_list_widget.setAlternatingRowColors(False)
        self.flashcard_list_widget.setIconSize(QtCore.QSize(345, 35))
        self.flashcard_list_widget.setTextElideMode(QtCore.Qt.ElideRight)
        self.flashcard_list_widget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.flashcard_list_widget.setGridSize(QtCore.QSize(350, 50))
        self.flashcard_list_widget.setViewMode(QtWidgets.QListView.IconMode)
        self.flashcard_list_widget.setObjectName("flashcard_list_widget")
        self.saved_title = QtWidgets.QLabel(self.saved_flashcards_page)
        self.saved_title.setGeometry(QtCore.QRect(350, 10, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.saved_title.setFont(font)
        self.saved_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.saved_title.setStyleSheet("background-color: rgba(233, 223, 245, 120);\n"
"color:rgb(77, 62, 122);\n"
"border-radius: 15px;")
        self.saved_title.setScaledContents(False)
        self.saved_title.setAlignment(QtCore.Qt.AlignCenter)
        self.saved_title.setObjectName("saved_title")
        self.go_back_2 = QtWidgets.QPushButton(self.saved_flashcards_page)
        self.go_back_2.setGeometry(QtCore.QRect(10, 10, 70, 50))
        self.go_back_2.setMinimumSize(QtCore.QSize(70, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.go_back_2.setFont(font)
        self.go_back_2.setStyleSheet("QPushButton {\n"
"    color:rgb(57, 41, 67);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgba(144, 130, 222, 120);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgba(133, 120, 206, 120);\n"
"}")
        self.go_back_2.setIconSize(QtCore.QSize(20, 20))
        self.go_back_2.setObjectName("go_back_2")
        self.Flashcard_content_2 = QtWidgets.QTextEdit(self.saved_flashcards_page)
        self.Flashcard_content_2.setGeometry(QtCore.QRect(440, 100, 491, 281))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Flashcard_content_2.setFont(font)
        self.Flashcard_content_2.setStyleSheet("QTextEdit {\n"
"    background-color: rgba(235, 235, 250, 130);\n"
"    border-radius: 20px;\n"
"    color: rgb(75, 54, 89);\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTextEdit::text {\n"
"    text-align: center;\n"
"}")
        self.Flashcard_content_2.setReadOnly(True)
        self.Flashcard_content_2.setObjectName("Flashcard_content_2")
        self.flashcard_number = QtWidgets.QTextEdit(self.saved_flashcards_page)
        self.flashcard_number.setGeometry(QtCore.QRect(660, 400, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.flashcard_number.setFont(font)
        self.flashcard_number.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.flashcard_number.setStyleSheet("background-color: rgba(235, 235, 250, 10);\n"
"border-radius: 20px;\n"
"color: rgb(77, 62, 122);")
        self.flashcard_number.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.flashcard_number.setReadOnly(True)
        self.flashcard_number.setObjectName("flashcard_number")
        self.previous_flashcard = QtWidgets.QPushButton(self.saved_flashcards_page)
        self.previous_flashcard.setGeometry(QtCore.QRect(550, 400, 70, 50))
        self.previous_flashcard.setMinimumSize(QtCore.QSize(70, 50))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(False)
        font.setWeight(50)
        self.previous_flashcard.setFont(font)
        self.previous_flashcard.setStyleSheet("QPushButton {\n"
"    color:rgb(57, 41, 67);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgba(144, 130, 222, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgba(133, 120, 206, 15);\n"
"}")
        self.previous_flashcard.setIconSize(QtCore.QSize(20, 20))
        self.previous_flashcard.setObjectName("previous_flashcard")
        self.next_flashcard = QtWidgets.QPushButton(self.saved_flashcards_page)
        self.next_flashcard.setGeometry(QtCore.QRect(750, 400, 70, 50))
        self.next_flashcard.setMinimumSize(QtCore.QSize(70, 50))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(False)
        font.setWeight(50)
        self.next_flashcard.setFont(font)
        self.next_flashcard.setStyleSheet("QPushButton {\n"
"    color:rgb(57, 41, 67);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgba(144, 130, 222, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgba(133, 120, 206, 15);\n"
"}")
        self.next_flashcard.setIconSize(QtCore.QSize(20, 20))
        self.next_flashcard.setObjectName("next_flashcard")
        self.delete_flashcard_button = QtWidgets.QPushButton(self.saved_flashcards_page)
        self.delete_flashcard_button.setGeometry(QtCore.QRect(570, 550, 230, 60))
        self.delete_flashcard_button.setMinimumSize(QtCore.QSize(220, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.delete_flashcard_button.setFont(font)
        self.delete_flashcard_button.setStyleSheet("QPushButton {\n"
"    color:rgb(77, 62, 122);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgba(251, 197, 220, 180);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgba(255, 186, 210, 200);\n"
"}")
        self.delete_flashcard_button.setIconSize(QtCore.QSize(20, 20))
        self.delete_flashcard_button.setObjectName("delete_flashcard_button")
        self.show_answer_button_2 = QtWidgets.QPushButton(self.saved_flashcards_page)
        self.show_answer_button_2.setGeometry(QtCore.QRect(570, 480, 230, 60))
        self.show_answer_button_2.setMinimumSize(QtCore.QSize(220, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.show_answer_button_2.setFont(font)
        self.show_answer_button_2.setStyleSheet("QPushButton {\n"
"    color:rgb(77, 62, 122);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgba(251, 197, 220, 180);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgba(255, 186, 210, 200);\n"
"}")
        self.show_answer_button_2.setIconSize(QtCore.QSize(20, 20))
        self.show_answer_button_2.setObjectName("show_answer_button_2")
        self.stackedWidget.addWidget(self.saved_flashcards_page)
        self.last_page = QtWidgets.QWidget()
        self.last_page.setStyleSheet("border-radius:15px;")
        self.last_page.setObjectName("last_page")
        self.backpic_4 = QtWidgets.QLabel(self.last_page)
        self.backpic_4.setGeometry(QtCore.QRect(0, 0, 950, 750))
        self.backpic_4.setMinimumSize(QtCore.QSize(900, 700))
        self.backpic_4.setStyleSheet("border-image: url(:/images/images/main_back.jpg);\n"
"border-radius:15px;")
        self.backpic_4.setText("")
        self.backpic_4.setObjectName("backpic_4")
        self.main_page_button = QtWidgets.QPushButton(self.last_page)
        self.main_page_button.setGeometry(QtCore.QRect(10, 10, 70, 50))
        self.main_page_button.setMinimumSize(QtCore.QSize(70, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.main_page_button.setFont(font)
        self.main_page_button.setStyleSheet("QPushButton {\n"
"    color:rgb(57, 41, 67);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgba(144, 130, 222, 120);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgba(133, 120, 206, 120);\n"
"}")
        self.main_page_button.setIconSize(QtCore.QSize(20, 20))
        self.main_page_button.setObjectName("main_page_button")
        self.get_answer_button = QtWidgets.QPushButton(self.last_page)
        self.get_answer_button.setGeometry(QtCore.QRect(661, 120, 220, 60))
        self.get_answer_button.setMinimumSize(QtCore.QSize(220, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.get_answer_button.setFont(font)
        self.get_answer_button.setStyleSheet("QPushButton {\n"
"    color:rgb(77, 62, 122);\n"
"}\n"
"QPushButton {\n"
"    background-color:rgb(173, 161, 238);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(151, 141, 204);\n"
"}")
        self.get_answer_button.setIconSize(QtCore.QSize(20, 20))
        self.get_answer_button.setObjectName("get_answer_button")
        self.enter_question_2 = QtWidgets.QTextEdit(self.last_page)
        self.enter_question_2.setGeometry(QtCore.QRect(70, 120, 550, 60))
        self.enter_question_2.setMinimumSize(QtCore.QSize(350, 40))
        self.enter_question_2.setMaximumSize(QtCore.QSize(550, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.enter_question_2.setFont(font)
        self.enter_question_2.setStyleSheet("background-color: rgba(233, 223, 245, 230);\n"
"border-radius: 15px;")
        self.enter_question_2.setMarkdown("")
        self.enter_question_2.setObjectName("enter_question_2")
        self.answer_to_question = QtWidgets.QTextEdit(self.last_page)
        self.answer_to_question.setGeometry(QtCore.QRect(70, 230, 811, 381))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.answer_to_question.setFont(font)
        self.answer_to_question.setStyleSheet("QTextEdit {\n"
"    background-color: rgba(235, 235, 250, 200);\n"
"    border-radius: 20px;\n"
"    color: rgb(75, 54, 89);\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTextEdit::text {\n"
"    text-align: center;\n"
"}")
        self.answer_to_question.setReadOnly(True)
        self.answer_to_question.setObjectName("answer_to_question")
        self.stackedWidget.addWidget(self.last_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Finals Project"))
        self.login_title.setText(_translate("MainWindow", "Log In"))
        self.username_1.setPlaceholderText(_translate("MainWindow", " User Name"))
        self.password_1.setPlaceholderText(_translate("MainWindow", " Password"))
        self.login_button.setText(_translate("MainWindow", "L o g I n"))
        self.go_to_signup_page.setText(_translate("MainWindow", "Do Not Have an Account? Create One"))
        self.signup_title.setText(_translate("MainWindow", "Sign Up"))
        self.email.setPlaceholderText(_translate("MainWindow", " Email"))
        self.username_2.setPlaceholderText(_translate("MainWindow", " User Name"))
        self.password_2.setPlaceholderText(_translate("MainWindow", " Password"))
        self.signup_button.setText(_translate("MainWindow", "Sign Up"))
        self.go_to_login_page.setText(_translate("MainWindow", "Go to Login Page"))
        self.enter_answer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.enter_answer.setPlaceholderText(_translate("MainWindow", " Enter the number of Questions"))
        self.flashcard_button.setText(_translate("MainWindow", "Generate"))
        self.go_back.setText(_translate("MainWindow", "⇦"))
        self.enter_question.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.enter_question.setPlaceholderText(_translate("MainWindow", " Enter theme of Questions"))
        self.next_flashcard_button.setText(_translate("MainWindow", "Next Flashcard"))
        self.save_flashcard_button.setText(_translate("MainWindow", "Save Flashcard"))
        self.show_answer_button.setText(_translate("MainWindow", "Show Answer"))
        self.go_to_Q_A.setText(_translate("MainWindow", "Q and A Page"))
        self.go_to_saved_flashcards.setText(_translate("MainWindow", "Saved Flashcards"))
        self.saved_title.setText(_translate("MainWindow", " Saved Flashcards"))
        self.go_back_2.setText(_translate("MainWindow", "⇦"))
        self.flashcard_number.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.previous_flashcard.setText(_translate("MainWindow", "↞"))
        self.next_flashcard.setText(_translate("MainWindow", "↠"))
        self.delete_flashcard_button.setText(_translate("MainWindow", "Delete Flashcard"))
        self.show_answer_button_2.setText(_translate("MainWindow", "Show Answer"))
        self.main_page_button.setText(_translate("MainWindow", "⇦"))
        self.get_answer_button.setText(_translate("MainWindow", "Answer"))
        self.enter_question_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.enter_question_2.setPlaceholderText(_translate("MainWindow", " Enter your question here"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
