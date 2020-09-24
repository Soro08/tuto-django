 # tuto-django 
![alt text](http://sdz.tdct.org/sdz/medias/uploads.siteduzero.com_files_250001_251000_250279.png)

# I- Comment installer django
  ## I-1 Intall Django mac os

##Setup 1

###Vérifier que python est installé 
:smile_cat:

```bash
$ python3
```
##Setup 2: créer un environnement virtuel
```bash
$ python3 -m venv venv
```
##Setup 3: activer l'environnement virtuel
```bash
$ source venv/bin/activate
```

##Setup 4:Installer Django

```bash
$ pip3 install Django
```
##Setup 6:Création de notre projet
> Django installé,:clap:

>On va créer un projet Django nommé myproject. :sunglasses:

```bash
$ django-admin startproject myproject
```

```python
myproject/
    bd.sqlite3        #Base de données par defaut
    manage.py         #manage.py va nous aider a lancer les commande
    myproject/        #application core
        __init__.py   #fichier init de python a ne pas supprimer
        settings.py   #fichier de configuration
        urls.py       #gestion de routage
        wsgi.py       #Utile pour le deploiement
```
##Setup 7: lancer le serveur django
> Le projet est créée. On va lancer notre première commande avec manage.py :runner:

```bash
$ cd myproject
$ python3 manage.py runserver
```



> Et notre application est lancé par défaut, elle ecoute sur le port 8000 :confetti_ball:

> Source [Django](https://docs.djangoproject.com/fr/2.2/intro/tutorial01/)



# II- Model et Admin
  ## II-1 Models
  
 ici nous allons profiter de l'ORM de django
 
 [Models](https://docs.djangoproject.com/fr/2.2/topics/db/models/)
 
 ```bash
    statut = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="post_article", null=true)
    
    python manage.py makemigrations
    python manage.py migrate
    
    pip freeze
    pip freeze > requirements.txt
 ```
 
 
 ### II-1-1 Models Query
 
 Ici le requette django avec ORM
 [QuerySet](https://docs.djangoproject.com/fr/2.2/ref/models/querysets/)
 
 ## II-2 Admin 
 
 ### II-2-1 (configuration)
 
 # Configuration du site django
 
 
 ```bash
 

 admin.site.site_header = "En tête du site" 
 admin.site.site_title = "Title"
 admin.site.index_title = "Message d'acceuil"
 
 
 
 
 
 ```
 
 ### II-2-2 Appel de models
 
 Exemple Basic de la partie admin
 
 ```bash
 from .models import *
 
 @admin.register(NomModel)
 class NomModelAdmin(admin.ModelAdmin):
     list_display = ('col1' ,'col2',)
     list_filter = ("col1",)
     search_fields = ('col1' ,'col2',)
     list_per_page = 50

     ordering = ['-col1', '-col2']

       
   ```
 
 ### FIchier static
 
 # settings.py
 
 ``` 
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

``` 

 # urls.py

``` 
from django.conf.urls.static import static
from django.conf import settings


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
 
 ``` 
 
 

@soro08 🇨🇮 :computer:
