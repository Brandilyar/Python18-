from User import User
from Blackjack import Card,Hand,Deck,new_game

print('Здравствуйте')

user = User.greet()
if user != False:
    print('Ваш логин: '+str(user.login)+', ваш пароль: '+str(user.password)+', ваш уникальный номер: '+str(user.uniq))
    answer = input('Вы хотите сыграть в игру Блэкджек yes/no? ')
    if answer == 'yes':
        print(new_game())
    else:
        print('До свидания')

else:
    print('До свидания')




    