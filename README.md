# tuto-django
Comment installer django
Intall Django mac os

##Setup 1

###Vérifier que python est installé

```bash
python3
```
##Setup 2: créer un environnement virtuel
```bash
python3 -m venv venv
```
##Setup 3: activer l'environnement virtuel
```bash
source venv/bin/activate
```

##Setup 4:Installer Django

```bash
pip3 install Django
```
##Setup 6:Création de notre projet
Django installé,

On va créer un projet Django nommé myproject.

```bash
django-admin startproject myproject
```
##Setup 7: lancer le serveur django
Le projet est créée. On va lancer notre première commande avec manage.py

```bash
cd myproject
python3 manage.py runserver
```



Et notre application est lancé par défaut, elle ecoute sur le port 8000
