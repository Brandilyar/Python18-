import re
import json

def load_data():
    try:
        file_path = 'data_user.json'
        with open(file_path) as file_data:
            return json.load(file_data)
    except:
        return {}

def validate(value):
    if re.search(r'^[a-zA-Z0-9]{8,}$', value):
        return value
    return False
def password():
    while True:
        password = input("Введите пароль: ")
        if validate(password):
            return password
        print('Не верный пароль') 
        continue   
def login():
    while True:
        login = input("Введите логин: ")
        if validate(login):
            if not users:
                return login
            elif login not in users:
                return login
            print('Логин занят. Придумайте другой')    
        else: 
            print('Логин не соответсвует правилам')      
        
        continue
print('Введите учетные данные. Логин и пароль могут содержать цифры и латинские буквы. Длина минумум 8 символов')
users = load_data()
login = login()
password = password()
users[login]=password
with open('data_user.json','w') as file_data:
    json.dump(users, file_data)


