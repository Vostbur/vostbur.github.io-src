Title: Установка netmiko в Windows
Date: 2020-04-02 23:00
Tags: windows, python, anaconda
Category: Меморизы

Модуль [netmiko](https://github.com/ktbyers/netmiko) дает красивый интерфейс поверх paramiko и telnetlib для подключения к сетевым устройствам по SSH или Telnet.  

Чтобы не связываться с установкой кучи всего от Microsoft для исправления ошибки "Microsoft Visual C++ 14.0 is required":  
1. Ставим [Miniconda](https://conda.io/en/latest/miniconda.html)  
2. Выполняем  
`conda install paramiko`  
`pip install netmiko`