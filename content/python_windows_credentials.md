Title: Сохранение паролей в Windows Credentials Locker из Python
Date: 2020-03-31 11:00
Tags: windows, python
Category: Меморизы

1. Ставим [keyring](https://pypi.org/project/keyring/)  
`pip install keyring` 

2. Выполняем  
`import keyring`  
`keyring.set_password("system", "username", "password")`  

3. Результат  
![Windows Credentials]({filename}/images/credentials.png)
  
4. Доступ к данным   
`keyring.get_password("system", "username")`  
`'password'` 

