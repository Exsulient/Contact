import sys
import sqlite3
import smtplib

from email.mime.text import MIMEText
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from newcontact import Ui_NewContact
from allcontact import Ui_all_contact
from sendmessage import Ui_sendmessage


class AllContact(QMainWindow, Ui_all_contact):
    def __init__(self):
        super(AllContact, self).__init__()
        uic.loadUi('allcontact.ui', self)
        self.pushButton.clicked.connect(self.open_newcontact)
        self.obnov.clicked.connect(self.obnova)
        self.connection = sqlite3.connect("contact.db")
        self.cur = self.connection.cursor()
        self.listWidget.clear()
        self.nameline_2.setEnabled(False)
        self.deletecontact.clicked.connect(self.delete_contact)
        self.deletecontact_2.clicked.connect(self.update)
        self.pushButton_3.clicked.connect(self.filter)
        self.pushButton_2.clicked.connect(self.delete_filter)
        rez = self.cur.execute("""select name, surname, phone, email, gender from Base_contact""").fetchall()
        for el in rez:
            if el[1] != '':
                n = (' '.join(str(i) for i in el))
                self.listWidget.addItem(n)
            else:
                list(el).pop(1)
                n = (' '.join(str(i) for i in el))
                self.listWidget.addItem(n)
        self.listWidget.itemDoubleClicked.connect(self.open_contact)
        self.sendemail.clicked.connect(self.send_mail)

    def open_newcontact(self):
        self.NewContactWindow = NewContact()
        self.NewContactWindow.show()

    def obnova(self):
        self.listWidget.clear()
        rez = self.cur.execute("""select name, surname, phone, email, gender from Base_contact""").fetchall()
        for el in rez:
            if el[1] != '':
                n = (' '.join(str(i) for i in el))
                self.listWidget.addItem(n)
            else:
                list(el).pop(1)
                n = (' '.join(str(i) for i in el))
                self.listWidget.addItem(n)

    def open_contact(self):
        n = self.listWidget.currentItem().text().split()
        if n[1][0] != '+':
            a = ' '.join(n[:2])
            self.nameline.setText(a)
            self.nameline_2.setText(n[2])
            self.nameline_3.setText(n[3])
        else:
            self.nameline.setText(n[0])
            self.nameline_2.setText(n[1])
            self.nameline_3.setText(n[2])

    def send_mail(self):
        self.sendmassgewindow = SendMessage()
        self.sendmassgewindow.show()

    def delete_contact(self):
        n = self.listWidget.currentItem().text().split()
        if n[1][0] != '+':
            phone = n[2]
            self.cur.execute("""delete from Base_contact where phone = ?""", (phone,)).fetchall()
            self.connection.commit()
            if self.man.isChecked() or self.radioButton_2.isChecked():
                self.filter()
            else:
                self.obnova()
            self.nameline.setText('')
            self.nameline_2.setText('')
            self.nameline_3.setText('')
        else:
            phone = n[1]
            self.cur.execute("""delete from Base_contact where phone = ?""", (phone,)).fetchall()
            self.connection.commit()
            if self.man.isChecked() or self.radioButton_2.isChecked():
                self.filter()
            else:
                self.obnova()
            self.nameline.setText('')
            self.nameline_2.setText('')
            self.nameline_3.setText('')

    def update(self):
        name = self.nameline.text()
        phone = self.nameline_2.text()
        email = self.nameline_3.text()
        print(name)
        n = name.split(' ')
        if len(n) > 0:
            name1 = n[0]
            surname = n[1]
            contact = (name1, surname, email, phone)
            self.cur.execute("""update Base_contact set name = ?, surname = ?, email = ? where phone = ?""", contact)
            self.connection.commit()
            self.obnova()
        else:
            surname = ''
            contact = (name, surname, email, phone)
            self.cur.execute("""update Base_contact set name = ?, surname = ?, email = ? where phone = ?""", contact)
            self.connection.commit()
            self.obnova()

    def filter(self):
        if self.man.isChecked():
            self.listWidget.clear()
            rez = self.cur.execute("""select name, surname, phone, email, gender from Base_contact 
            where gender = 'Мужской'""").fetchall()
            for el in rez:
                if el[1] != '':
                    n = (' '.join(str(i) for i in el))
                    self.listWidget.addItem(n)
                else:
                    list(el).pop(1)
                    n = (' '.join(str(i) for i in el))
                    self.listWidget.addItem(n)
        else:
            self.listWidget.clear()
            rez = self.cur.execute("""select name, surname, phone, email, gender from Base_contact 
            where gender = 'Женский'""").fetchall()
            for el in rez:
                if el[1] != '':
                    n = (' '.join(str(i) for i in el))
                    self.listWidget.addItem(n)
                else:
                    list(el).pop(1)
                    n = (' '.join(str(i) for i in el))
                    self.listWidget.addItem(n)

    def delete_filter(self):
        self.man.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.obnova()


class NewContact(QMainWindow, Ui_NewContact):
    def __init__(self):
        super().__init__()
        uic.loadUi('newcontact.ui', self)
        self.label = QLabel(self)
        self.pixmap = QPixmap('people.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(150, 150)
        self.label.move(60, 20)
        self.show()
        self.phone.setText('+7')
        self.countryphone.currentTextChanged.connect(self.country)
        self.AddContact.clicked.connect(self.Newcontact)
        self.man.setChecked(True)
        self.connection = sqlite3.connect("contact.db")
        self.cur = self.connection.cursor()

    def country(self, text):
        self.phone.setText(text[text.index('+'):])

    def Newcontact(self):
        name = self.name.text()
        surname = self.fname.text()
        phone = self.phone.text()
        email = self.email.text()
        if name != '' and phone != '':
            self.AddContact.setText('Добавить контакт')
            if self.man.isChecked():
                gender = 'Мужской'
            else:
                gender = 'Женский'
            contact = (name, surname, phone, email, gender)
            n = self.cur.execute("""select phone from Base_contact where phone = ?""", (phone, )).fetchall()
            if n == []:
                self.cur.execute("""INSERT INTO Base_contact(name, surname, phone, email, gender)
                VALUES(?, ?, ?, ?, ?);""", contact)
                self.connection.commit()
                self.connection.close()
                self.close()
            else:
                self.AddContact.setText('Номер уже есть')
        else:
            self.AddContact.setText('Заполните всю \n необходимую \n информацию')

class SendMessage(QMainWindow, Ui_sendmessage):
    def __init__(self):
        super().__init__()
        uic.loadUi('sendmessage.ui', self)
        self.pushButton.clicked.connect(self.send_message)

    def send_message(self):
        sender = "yandexsendmessage@gmail.com"
        password = "luguxoxsnbwsdovd"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        try:
            server.login(sender, password)
            msg = MIMEText(self.textEdit.text())
            msg["Subject"] = self.lineEdit_3.text()
            server.sendmail(sender, self.lineEdit_2.text(), msg.as_string())

            self.close()
        except Exception as _ex:
            return 'Ошибка'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AllContact()
    ex.show()
    sys.exit(app.exec_())
