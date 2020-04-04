Title: Подключение к устаревшим Cisco по SSH
Date: 2020-04-04 22:20
Tags: network, cisco, linux, SSH
Category: Меморизы

Если при попытке подключиться выдает что-то похожее на "no matching key exchange method found":  

_На Cisco (ip 192.168.2.2)_:  
- длина ключа RSA должна быть больше 1024  
- создаем учетную запись пользователя (здесь - cisco)  

_В Ubuntu_:  
- создаем ~/.ssh/config  
> Host 192.168.2.2  
>> KexAlgorithms +diffie-hellman-group1-sha1  
>> Ciphers aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc  

Алгоритмы могут быть другие, подходящие будут указаны в сообщении об ошибке.  
- проверяем  
`ssh 192.168.2.2 -l cisco`  

Еще почитать [здесь](https://4admin.info/legacy-ssh-device/).