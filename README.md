### SETUP
create .env file in InstaBot/.env :

```
INSTAGRAM_USERNAME=*********
INSTAGRAM_PASSWORD=*********
```

data/file/cualquier_nombre.png  <br />
data/messagge/cualquier_nombre.txt  <br />
data/usernames/cualquier_nombre.txt  <br />

### RUN
To launch the script:

```
python app.py file message video
```

**file**:  <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Que: Cualquier file en data/file/  <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Formato: PNG, JPEG, PDF ...  <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;El nombre del fichiero no importa
 
**message**:  <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Que: Cualquier file en data/messages/  <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Formato: .txt  <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;El nombre del fichiero no importa    

**video**:  <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Al inicio, tendra que anadir el videoId (ex: Cau0Ahxjf1v)  <br />


El file y message sera enviado en el mismo tiempo a cada uno de los usuario de la lista.  <br />
La video sera enviado despues, en una segunda iteration.

### TODO

- structured text

