'''
написать приложение-сервер используя модуль socket работающее в домашней 
локальной сети.
Приложение должно принимать данные с любого устройства в сети отправленные 
или через программу клиент или через браузер
    - если данные пришли по протоколу http создать возможность след.логики:
        - если путь содержит /test/<int>/ вывести сообщение - тест с номером int запущен
        
        - если путь содержит message/<login>/<text>/ вывести в консоль сообщение
            "{дата время} - сообщение от пользователя {login} - {text}"
        
        - во всех остальных случаях вывести сообщение:
            "пришли неизвестные  данные по HTTP - путь такой то"
                   
        
    - если данные пришли НЕ по протоколу http создать возможность след.логики:
        - если пришла строка формата "command:reg; login:<login>; password:<pass>"
            - выполнить проверку:
                login - только латинские символы и цифры, минимум 6 символов
                password - минимум 8 символов, должны быть хоть 1 цифра
            - при успешной проверке:
                1. вывести сообщение: 
                    "{дата время} - пользователь {login} {password} зарегистрирован"
                2. добавить данные пользователя в список/словарь
            - если проверка не прошла вывести сообщение:
                "{дата время} - ошибка регистрации {login} - неверный пароль/логин"
                
        - если пришла строка формата "command:signin; login:<login>; password:<pass>"
            выполнить проверку зарегистрирован ли такой пользователь:                
            
            при успешной проверке:
                1. вывести сообщение: 
                    "{дата время} - пользователь {login} произведен вход"
                
            если проверка не прошла вывести сообщение
                "{дата время} - ошибка входа {login} - неверный пароль/логин"
        
        - во всех остальных случаях вывести сообщение:
            "пришли неизвестные  данные - <присланные данные>"            

'''