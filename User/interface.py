from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from User import User,Validate
from Blackjack import Card,Hand,Deck,new_game
import json
import time

qt_main_file = 'mainwindow.ui'
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_main_file)


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.textEdit.hide()
        self.radioButton.hide()
        self.radioButton_2.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        self.label.hide()
        self.label_2.hide()
        self.Label.hide()
        self.Label_2.hide()
        self.Label_3.hide()
        self.Label_4.hide()
        self.LineEdit.hide()
        self.LineEdit_2.hide()
        self.LineEdit_3.hide()
        self.LineEdit_4.hide()
        self.dockWidget.hide()
        self.LineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.hide()
        
    def get_login(self):
        # Формирование диалогового окна. Зарегистрирован ли пользователь.
        widgets = [self.label_2,self.radioButton,self.radioButton_2,self.pushButton_3]
        for one_widget in widgets:
            one_widget.show()
        self.pushButton_3.clicked.connect(lambda:self.check(widgets))
    def check(self,widgets):
        # Проверка какой ответ дан.
        if self.radioButton.isChecked()==True:
            for one_widget in widgets:
                one_widget.hide()
            self.login()
        if self.radioButton_2.isChecked()==True:
            for one_widget in widgets:
                one_widget.hide()
            self.registration(widgets)

    def login(self,widgets=[]):
        # Формирование окна авторизации
        self.dockWidget.hide()
        self.pushButton_4.hide()
        for one_widget in widgets:
            one_widget.hide()
        widgets = [self.Label,self.Label_2,self.LineEdit,self.LineEdit_2,self.pushButton]
        for one_widget in widgets:
            one_widget.show()        
        self.pushButton.clicked.connect(lambda:self.valid_login(widgets))
    def valid_login(self,widgets):
        # Проверка учетных данных пользователя
        login = self.LineEdit.text()
        password = self.LineEdit_2.text()
        data = User.get_users_data()
        user = data.get(login)
        if user != None:
            if data[login]['password'] == password:
                for one_widget in widgets:
                    one_widget.hide()
                self.main()
            else:
                self.label_3.setText('Неверные учетные данные.')
                self.dockWidget.show()
        else:
            self.label_3.setText('Пользователь с указанными учетными данными не найден.')
            self.pushButton_4.show()
            self.dockWidget.show()
            self.pushButton_4.clicked.connect(lambda:self.registration(widgets))
    def registration(self,widgets):
        # Формирование окна регистрации
        self.dockWidget.hide()
        self.pushButton_4.hide()
        for one_widget in widgets:
            one_widget.hide()
        widgets = [self.label,self.Label_3,self.Label_4,self.LineEdit_3,self.LineEdit_4,self.pushButton_2]
        for one_widget in widgets:
            one_widget.show()                       
        self.pushButton_2.clicked.connect(lambda:self.valid_registration(widgets))
    def valid_registration(self,widgets):
        # Проверка данных для регистрации
        login = self.LineEdit_3.text()
        password = self.LineEdit_4.text()
        user = User(login,password)
        valid = Validate(login,password)
        if valid.validate_login() and valid.validate_password:
            data_users = user.get_users_data()
            if login not in data_users:
                data_users[login]={'password':password,'uniq':user.uniq}
                with open('data_user.json','w') as file_data:
                    json.dump(data_users, file_data)
                self.label_3.setText('Вы успешно зарегистрированы.')
                self.pushButton_4.setText('Войти?')
                self.pushButton_4.show()
                self.dockWidget.show()
                self.pushButton_4.clicked.connect(lambda:self.login(widgets))
            else:
                self.label_3.setText('Пользователь с данными учетными данными уже зарегистрирован.')
                self.dockWidget.show()
        else:
            self.label_3.setText('Ваши данные не прошли проверку')
            self.dockWidget.show()
    def main(self):
        # Формирование основного окна
        self.dockWidget.hide()
        widgets = [self.textEdit,self.lineEdit,self.pushButton_5]
        for one_widget in widgets:
            one_widget.show()
        self.start_game()
        

    def start_game(self):
        # создаем колоду
        d = Deck()
        # задаем "руки" для игрока и дилера
        player_hand = Hand("Player")
        dealer_hand = Hand("Dealer")
        # сдаем две карты игроку
        player_hand.add_card(d.deal_card())
        player_hand.add_card(d.deal_card())
        # сдаем одну карту дилеру
        dealer_hand.add_card(d.deal_card())
        self.textEdit.append(str(dealer_hand))
        self.textEdit.append(str("="*20))
        self.textEdit.append(str(player_hand))
        # Флаг проверки необходимости продолжать игру
        in_game = True
        # набирать карты игроку имеет смысл только если у него на руке меньше 21 очка
        self.textEdit.append("Hit or stand? (h/s) ")
        self.pushButton_5.clicked.connect(lambda:self.game(d,player_hand,dealer_hand,in_game))

    def game(self,d,player_hand,dealer_hand,in_game):                        
        if player_hand.get_value() < 21:           
            answer = self.lineEdit.text()                                          
            if answer== "h":
                player_hand.add_card(d.deal_card())
                self.textEdit.append(str(player_hand))       
                self.textEdit.append("Hit or stand? (h/s) ")               
                # Если у игрока перебор - дилеру нет смысла набирать карты
                if player_hand.get_value() > 21:
                    self.textEdit.append("You lose")
                    in_game = False
                    self.dealer(d,player_hand,dealer_hand,in_game)
            else:
                self.textEdit.append("You stand!")
                self.dealer(d,player_hand,dealer_hand,in_game)
        self.textEdit.append("=" * 20)
    def dealer(self,d,player_hand,dealer_hand,in_game):
        if in_game:
            # По правилам дилер обязан набирать карты пока его счет меньше 17
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(d.deal_card())
                self.textEdit.append(str(dealer_hand))
                # Если у дилера перебор играть дальше нет смысла - игрок выиграл
                if dealer_hand.get_value() > 21:
                    self.textEdit.append("Dealer bust")
                    in_game = False
        if in_game:
            # Ни у кого не было перебора - сравниваем количество очков у игрока и дилера. 
            # В нашей версии если у дилера и игрока равное количество очков - выигрывает казино
            if player_hand.get_value() > dealer_hand.get_value():
                self.textEdit.append("You win")
            else:
                self.textEdit.append("Dealer win")


app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.get_login()
main.show()
sys.exit(app.exec())