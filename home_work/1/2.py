"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""



import string
great = string.ascii_letters + string.digits + "_"

def check_login(user):
    for c in user['login']:
        if not c in great:            
            return False
    return True

users = [
    {"name":"some_name1", "login":"some_login1!", "password":"123456" },
    {"name":"some_name2", "login":"some_login2", "password":"1234" },
    {"name":"some_name3", "login":"some_login3", "password":"12345678" },
    {"name":"some_name4", "login":"some_login4@", "password":"123" }
]

bad_pas = list(filter(lambda x:len(x['password'])<5, users))
print(*bad_pas, sep="\n")
print()

# варианты с lambda
# bad_login = list(filter(lambda x: list(filter(lambda x:not x in great, x['login'])), users))
# bad_login = list(filter(lambda x: any(map(lambda x: not x in great, x['login'])), users))

gr_login = list(filter(check_login, users))
print(*gr_login, sep="\n")