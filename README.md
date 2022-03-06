### SETUP
create .env file in InstaBot/.env :

```
INSTAGRAM_USERNAME=*********
INSTAGRAM_PASSWORD=*********
```

data/file/*.png
data/messagge/*.txt
data/usernames/*.txt

### RUN
To launch the script:

```
python app.py file message video
```

OPTION file:
    Que: Cualquier file en data/file/
    Formato: PNG, JPEG, PDF ...
    El nombre del fichiero no importa

OPTION message:
    Que: Cualquier file en data/messages/
    Formato: .txt
    El nombre del fichiero no importa    

OPTION video:
    Al inicio, tendra que anadir el videoId (ex: Cau0Ahxjf1v) 


El file y message sera enviado en el mismo tiempo a cada uno de los usuario de la lista.
La video sera enviado despues, en una segunda iteration.


### TODO

- structured text

