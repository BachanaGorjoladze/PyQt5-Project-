import google.generativeai as genai
import bcrypt
from dotenv import load_dotenv
import os
import sqlite3
from PyQt5 import QtWidgets
from final import Ui_MainWindow
from database import create_connection, create_tables
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from google_authentication import get_authorization_url, fetch_user_info

load_dotenv()
API_key = os.getenv("API_key")

genai.configure(api_key=API_key)
model = genai.GenerativeModel("gemini-1.5-flash")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.auth_url = get_authorization_url()
        self.browser = QWebEngineView()

        self.array = []
        self.index = 0
        self.disable_flashcard_buttons()

        self.ui.go_to_signup_page.clicked.connect(self.switch_to_signup_page)
        self.ui.go_to_login_page.clicked.connect(self.switch_to_login_page)
        self.ui.login_button.clicked.connect(self.login)
        self.ui.signup_button.clicked.connect(self.sign_up)
        self.ui.go_back.clicked.connect(self.switch_to_login_page)
        self.ui.main_page_button.clicked.connect(self.switch_to_main_page)
        self.ui.go_to_Q_A.clicked.connect(self.switch_to_last_page)
        self.ui.go_to_saved_flashcards.clicked.connect(
            self.saved_flashcards_page)
        self.ui.go_back_2.clicked.connect(self.switch_to_main_page)

        self.ui.flashcard_list_widget.itemClicked.connect(
            self.load_selected_flashcard)
        self.ui.show_answer_button_2.clicked.connect(self.show_saved_answer)
        self.ui.delete_flashcard_button.clicked.connect(self.delete_flashcard)

        self.ui.previous_flashcard.clicked.connect(
            self.show_previous_flashcard)
        self.ui.next_flashcard.clicked.connect(self.show_next_flashcard)

        try:
            self.conn = create_connection('users.db')
            create_tables(self.conn)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"Error while connecting to the database: {e}")

        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)
        self.ui.flashcard_button.clicked.connect(self.generate_display)

        self.ui.next_flashcard_button.clicked.connect(self.show_question)
        self.ui.show_answer_button.clicked.connect(self.show_answer)

        self.ui.main_page_button.clicked.connect(self.reset_index)
        self.ui.save_flashcard_button.clicked.connect(self.save_questions)
        self.ui.get_answer_button.clicked.connect(self.generate_answer)

        self.final_url = None
        self.ui.google_auth.clicked.connect(self.open_google_signin)
        self.browser.urlChanged.connect(self.get_email_name)

    def open_google_signin(self):
        try:
            self.credentials = None

            self.browser = QWebEngineView()

            self.browser_window = QtWidgets.QWidget()
            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(self.browser)
            self.browser_window.setLayout(layout)
            self.browser_window.setWindowTitle("Google Sign-In")
            self.browser_window.resize(800, 600)
            self.browser_window.setWindowIcon(QIcon('images/Google_icon.png'))
            self.browser_window.show()
            self.browser.setUrl(QUrl(self.auth_url))

            self.browser.urlChanged.connect(self.get_email_name)

        except Exception as e:
            print(f"Error opening Google sign-in page: {e}")

    def get_email_name(self, url):
        self.final_url = ''
        if "localhost:8080" in url.toString():
            self.final_url = url.toString()
            self.browser_window.close()

        if self.final_url:
            info = fetch_user_info(self.final_url)
            self.name = info[0]
            self.email = info[1]
            self.login_name = self.name
            self.switch_to_main_page()

    def save_questions(self):
        if not (0 <= self.index < len(self.array)):
            raise IndexError("index out of bounds for the arrary")

        if self.index % 2 == 0:
            self.saved_question = self.array[self.index]
            self.saved_answer = self.array[self.index + 1]
        else:
            self.saved_question = self.array[self.index - 1]
            self.saved_answer = self.array[self.index]

        self.cursor.execute(
            "SELECT MAX(question_number) FROM questions WHERE username=?", (self.login_name,))
        row = self.cursor.fetchone()

        if row[0] is not None:
            self.next_question_number = row[0] + 1
        else:
            self.next_question_number = 1

        try:
            self.cursor.execute("INSERT INTO questions (username, question_number, question, answer) VALUES (?, ?, ?, ?)",
                                (self.login_name, self.next_question_number, self.saved_question, self.saved_answer))
            self.conn.commit()
            self.ui.Flashcard_content.setPlainText(
                "Question saved successfully")
        except sqlite3.IntegrityError:
            self.ui.Flashcard_content.setPlainText(
                "You have already saved this question")

    def encrypt_password(self, password: str):
        password_bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed_password.decode('utf-8')

    def is_valid_email(self, email):
        import re
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_regex, email) is not None

    def sign_up(self):
        self.user_email = self.ui.email.text().strip()
        self.user_username = self.ui.username_2.text().strip()
        self.user_uncoded_password = self.ui.password_2.text().strip()

        self.user_password = self.encrypt_password(self.user_uncoded_password)

        if not self.user_email or not self.user_username or not self.user_password:
            self.ui.signup_label.setText("Please fill in all fields.")
            self.clear_signup()
            return

        if not self.is_valid_email(self.user_email):
            self.ui.signup_label.setText("Please enter a valid email address.")
            self.clear_signup()
            return

        try:
            self.cursor.execute(
                "SELECT * FROM users WHERE username=?", (self.user_username,))
            if self.cursor.fetchone():
                self.ui.signup_label.setText("Username already exists.")
                self.clear_signup()
                return

            self.cursor.execute("INSERT INTO users (email, username, password) VALUES (?, ?, ?)",
                                (self.user_email, self.user_username, self.user_password))
            self.conn.commit()

            self.ui.login_label.setText("")
            self.ui.signup_label.clear()
            self.switch_to_login_page()

        except sqlite3.Error as e:
            print(f"Error: {e}")

        self.clear_signup()

    def login(self):

        self.login_name = self.ui.username_1.text()
        self.login_password = self.ui.password_1.text()

        try:
            self.cursor.execute(
                "SELECT * FROM users WHERE username=?", (self.login_name,))
            row = self.cursor.fetchone()

            if row:
                stored_password = row[2]
                if bcrypt.checkpw(self.login_password.encode('utf-8'), stored_password.encode('utf-8')):
                    self.switch_to_main_page()
                    self.ui.login_label.clear()
                else:
                    self.ui.login_label.setText("invalid username or password")
            else:
                self.ui.login_label.setText("invalid username or password")

        except sqlite3.Error as e:
            print(f"Error : {e}")

        self.ui.username_1.clear()
        self.ui.password_1.clear()

    def get_number(self):
        self.num = self.ui.enter_answer.toPlainText()
        if self.num.strip() == "":
            self.num_questions = None
        else:
            try:
                self.num_questions = int(self.num)
            except ValueError:
                self.num_questions = None

    def get_text(self):
        self.keyword = self.ui.enter_question.toPlainText()
        if self.keyword.strip() == "":
            self.keyword = None

    def generate_display(self):
        self.get_text()
        self.get_number()
        self.ui.enter_question.clear()
        self.ui.enter_answer.clear()
        self.reset_index()

        if self.keyword and self.num_questions and self.num_questions <= 30:
            self.generate_questions()
            self.enable_flashcard_buttons()

            if self.array:
                self.ui.Flashcard_content.setPlainText(self.array[0])
            else:
                self.ui.Flashcard_content.setPlainText(
                    "No questions generated.")
        else:
            self.ui.Flashcard_content.setPlainText(
                "Please provide both the theme and correct number of questions (30 is maximum)")
            self.disable_flashcard_buttons()

    def generate_answer(self):
        self.question = self.ui.enter_question_2.toPlainText()
        if self.question.strip() == "":
            self.question = None

        self.ui.enter_question_2.clear()
        self.answer_prompt = f"Generate a simple and direct answer that is less than 170 words to this question : {self.question}"

        if self.question == None:
            self.ui.answer_to_question.setPlainText(
                "Please provide a question")
        else:
            try:
                response = model.generate_content(self.answer_prompt)
                answer_text = response.text
                self.ui.answer_to_question.setPlainText(answer_text)
            except Exception as e:
                self.ui.answer_to_question.setPlainText(
                    f"An error occurred: {str(e)}")

    def generate_questions(self):
        self.prompt = f"""Generate a simple and direct question about the topic of "{self.keyword}". 
                            Then provide a correct answer to the question. Output the question on one line
                            and the answer on the next line and another question on the next line
                            and do this {self.num_questions} times. do this once for every question.
                            """
        try:
            if int(self.num_questions) <= 0:
                self.ui.Flashcard_content.setPlainText(
                    "Please provide a valid positive number of question-answer pairs.")
            else:
                response = model.generate_content(self.prompt)
                lines = response.text.strip().split('\n')

                self.array = []
                for i in range(0, min(len(lines), 2 * int(self.num_questions)), 2):
                    question = lines[i].strip()
                    if i + 1 < len(lines):
                        answer = lines[i + 1].strip()
                        self.array.append(question)
                        self.array.append(answer)

                if len(self.array) // 2 < int(self.num_questions):
                    print("Not enough question-answer pairs were generated.")
        except ValueError:
            print("Please provide a valid number of questions.")

    def show_question(self):
        """ გამოიყენება კითხვების ჩვენებისთვის self.array სიიდან """
        self.ui.show_answer_button.setDisabled(False)

        if self.index % 2 == 0:
            self.index += 2
        else:
            self.index += 1

        if self.index >= len(self.array):
            self.ui.Flashcard_content.setPlainText("No more Questions")
            self.disable_flashcard_buttons()
        else:
            self.ui.Flashcard_content.setPlainText(self.array[self.index])

    def show_answer(self):
        self.ui.show_answer_button.setDisabled(True)
        if self.index < len(self.array) - 1:

            if not hasattr(self, 'showing_answer'):
                self.showing_answer = False

            question = self.array[self.index]
            answer = self.array[self.index + 1]

            if self.showing_answer:
                self.ui.Flashcard_content.setPlainText(
                    question)
                self.showing_answer = False
            else:
                self.ui.Flashcard_content.setPlainText(
                    answer)
                self.showing_answer = True

        self.ui.show_answer_button.setDisabled(False)

    def reset_index(self):
        self.index = 0

    def clear_signup(self):
        self.ui.email.clear()
        self.ui.username_2.clear()
        self.ui.password_2.clear()

    def disable_flashcard_buttons(self):
        self.ui.next_flashcard_button.setDisabled(True)
        self.ui.save_flashcard_button.setDisabled(True)
        self.ui.show_answer_button.setDisabled(True)

    def enable_flashcard_buttons(self):
        self.ui.next_flashcard_button.setDisabled(False)
        self.ui.save_flashcard_button.setDisabled(False)
        self.ui.show_answer_button.setDisabled(False)

    def switch_to_signup_page(self):
        self.ui.login_label.setText("")
        self.ui.username_1.clear()
        self.ui.password_1.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.signup_page)

    def switch_to_login_page(self):
        self.ui.signup_label.setText("")
        self.ui.Flashcard_content.clear()
        self.disable_flashcard_buttons()
        self.clear_signup()
        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)

    def switch_to_main_page(self):
        self.ui.enter_question.clear()
        self.ui.enter_answer.clear()
        self.ui.Flashcard_content.clear()
        self.ui.answer_to_question.clear()
        self.ui.Flashcard_content_2.clear()
        self.ui.flashcard_number.clear()
        self.disable_flashcard_buttons()
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_page)

    def saved_flashcards_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.saved_flashcards_page)
        self.ui.flashcard_list_widget.clear()

        try:
            self.cursor.execute(
                "SELECT question, answer FROM questions WHERE username = ? LIMIT 100", (self.login_name,))
            rows = self.cursor.fetchall()

            for question, answer in rows:
                item = QtWidgets.QListWidgetItem(f"Q: {question}\nA: {answer}")
                self.ui.flashcard_list_widget.addItem(item)
        except sqlite3.Error as e:
            print(f"Error while saving flashcards: {e}")

    def switch_to_last_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.last_page)

    def load_selected_flashcard(self, item):
        text = item.text()
        question, answer = text.split("\nA: ")
        question = question.replace("Q: ", "")

        self.current_flashcard = (question, answer)
        self.ui.Flashcard_content_2.setPlainText(question)

        self.cursor.execute("SELECT question_number FROM questions WHERE username=? AND question=?",
                            (self.login_name, question))
        row = self.cursor.fetchone()

        if row:
            self.current_flashcard_number = row[0]
            self.ui.flashcard_number.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.flashcard_number.setFont(
                QtGui.QFont("Arial", 20, QtGui.QFont.Bold))
            self.ui.flashcard_number.setPlainText(str(row[0]))

        self.current_index = self.ui.flashcard_list_widget.row(item)

    def show_saved_answer(self):
        if hasattr(self, 'current_flashcard'):
            question, answer = self.current_flashcard

            if self.ui.Flashcard_content_2.toPlainText() == question:
                self.ui.Flashcard_content_2.setPlainText(
                    answer)
            else:
                self.ui.Flashcard_content_2.setPlainText(
                    question)

    def delete_flashcard(self):
        if hasattr(self, 'current_flashcard'):
            question, _ = self.current_flashcard

            self.cursor.execute("DELETE FROM questions WHERE username=? AND question=?",
                                (self.login_name, question))
            self.conn.commit()

            for i in range(self.ui.flashcard_list_widget.count()):
                item = self.ui.flashcard_list_widget.item(i)
                if item.text().startswith(f"Q: {question}"):
                    self.ui.flashcard_list_widget.takeItem(i)
                    break

            self.ui.Flashcard_content_2.clear()
            self.ui.flashcard_number.clear()

    def show_next_flashcard(self):
        if hasattr(self, 'current_index'):
            if self.current_index < self.ui.flashcard_list_widget.count()-1:
                self.current_index += 1
                item = self.ui.flashcard_list_widget.item(self.current_index)
                if item:
                    self.load_selected_flashcard(item)

    def show_previous_flashcard(self):
        if hasattr(self, 'current_index'):
            if self.current_index > 0:
                self.current_index -= 1
                item = self.ui.flashcard_list_widget.item(self.current_index)
                if item:
                    self.load_selected_flashcard(item)

    def closeEvent(self, event):
        try:
            if self.conn:
                self.conn.close()

        except sqlite3.Error as e:
            print(f"Error : {e}")

        finally:
            event.accept()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
