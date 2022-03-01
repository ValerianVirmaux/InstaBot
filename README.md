sudo docker image ls
sudo docker run -it -e ENVIRONMENT=DEV -e USERNAME=forro.pirata.bcn -e PASSWORD=forrodasininho fd309b8a2006 /bin/bash
python3 app.py