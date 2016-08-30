#I'm Learning Python

##Requirements

Run the Neo4J latest image
https://hub.docker.com/_/neo4j/
and of course populate the graph with demo data provided

Create a `config.ini` file from `config.ini.dist` with your the parameter

##Run the app
In your terminal

```
python3 -m venv m-env
source m-env/bin/activate
pip3 install -r requirements.txt

python3 app.py
```

and then go to
```
http://localhost:_yourport_/v1.0/ui/
```
