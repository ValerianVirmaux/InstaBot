### SETUP
create .env file in InstaBot/.env :

```
INSTAGRAM_USERNAME=*********
INSTAGRAM_PASSWORD=*********
```

data/file/*.png  <br />
data/messagge/*.txt  <br />
data/usernames/*.txt  <br />

### RUN
To launch the script:

```
python app.py file message video
```

**file**:  <br />
    Que: Cualquier file en data/file/  <br />
    Formato: PNG, JPEG, PDF ...  <br />
    El nombre del fichiero no importa
 
**message**:  <br />
    Que: Cualquier file en data/messages/  <br />
    Formato: .txt  <br />
    El nombre del fichiero no importa    

**video**:  <br />
    Al inicio, tendra que anadir el videoId (ex: Cau0Ahxjf1v)  <br />


El file y message sera enviado en el mismo tiempo a cada uno de los usuario de la lista.  <br />
La video sera enviado despues, en una segunda iteration.


### TODO

- structured text

