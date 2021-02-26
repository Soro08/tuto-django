# Django

#Usage:
Install djongo:
```bash pip install djongo  ``` 

Into settings.py file of your project, add:

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your-db-name',
        'CLIENT': {
           'host': 'your-db-host',
        }
    }
}

``` 
