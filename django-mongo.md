# Django

## Usage:
Install djongo:

```python 
pip install djongo  
``` 

Into settings.py file of your project, add:

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': {
            'host': '',
            "authMechanism": "SCRAM-SHA-1",
        }
    }
}

``` 

Istall DNS PYTHON

```python
pip install dnspython
```
