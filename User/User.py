import json
import re
import random


class User:      
    def __init__(self,login,password,uniq = random.randint(1,1000)):
        '''Инициализация класса User с атрибудами login и пароль'''
        self.login = login
        self.password = password
        self.uniq = uniq
    @staticmethod
    def get_users_data():
        '''Получение базы данных пользователей'''
        try:
            file_path = 'data_user.json'
            with open(file_path) as file_data:
                return json.load(file_data)
        except:
            return {}
    @staticmethod
    def get_user(login,password):
        '''Поиск пользователя в базе данных'''
        data = User.get_users_data()
        user_data = data.get(login)
        if user_data != None:
            if data[login]['password'] == password:
                return User(login,data[login]['password'],data[login]['uniq'])
            else:
                print('Неверные учетные данные')
                return False
        '''else:
            print('Пользователь с указанными учетными данными не найден')
            print('Логин и пароль должны содержать минимум 8 символов. Допустимы латинские буквы и цифры от 0 до 9')
            answer_reg = input ('Вы хотите зарегистрироваться yes/no? ')                
            if answer_reg == 'yes':
                return User.registration(login,password)
            return False'''
    

   

class Validate:

    def __init__(self,login,password):
        self.login = login
        self.password = password

    def validate_login(self):
        if re.search(r'^[a-zA-Z0-9]{8,}$', self.login):
            return True
        return False
    def validate_password(self):
        if re.search(r'^[a-zA-Z0-9]{8,}$', self.password):
            return True
        return False





 

  
        
 


