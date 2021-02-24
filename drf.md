 # tuto-django-rest-framework
![alt text](https://soshace.com/wp-content/uploads/2021/01/879-png-3.png)

## configurations

```
    Nous suggerons que vous avez creer un projet django et faire sa configuration avec une application
```

### Installations
```python
    pip install djangorestframework
    # Dans le fichier setting.py
    INSTALLED_APPS = (
    ...
    'rest_framework',
    )
```

### Creation de models
```python
    from django.db import models
    from django.contrib.auth.models import User


    class Poll(models.Model):
        question = models.CharField(max_length=100)
        created_by = models.ForeignKey(User, on_delete=models.CASCADE)
        pub_date = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.question


    class Choice(models.Model):
        poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=100)

        def __str__(self):
            return self.choice_text
    
    # Migrations des models
    python manage.py makemigrations
    python manage.py migrate

```
## Creer une API avec Django pure
```python
    # Dans le fichier views.py
    from django.shortcuts import render, get_object_or_404
    from django.http import JsonResponse

    from .models import Poll

    def polls_list(request):

        MAX_OBJECTS = 20
        polls = Poll.objects.all()[:MAX_OBJECTS]
        data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
        return JsonResponse(data)

    def polls_detail(request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        data = {"results": {
            "question": poll.question,
            "created_by": poll.created_by.username,
            "pub_date": poll.pub_date
        }}
        return JsonResponse(data)


    # Dans le fichier urls.py
    from django.urls import path
    from .views import polls_list, polls_detail

    urlpatterns = [
        path("polls/", polls_list, name="polls_list"),
        path("polls/<int:pk>/", polls_detail, name="polls_detail")
    ]
```
## Creer une API avec Django Rest Framework

```
    Pour creer une API avec DRF on a 4 etapes:
    -La serialisation des données
    -La creation des APIVIEWS ou VIEWSET
    -La creation des routes

```
```
    LA SERIALISATION
    creer un fichier serializers.py dans l application du projet
    
```

```python
    from rest_framework import serializers
    from .models import Poll, Choice

    class ChoiceSerializer(serializers.ModelSerializer):
        votes = VoteSerializer(many=True, required=False)

        class Meta:
            model = Choice
            fields = '__all__'


    class PollSerializer(serializers.ModelSerializer):
        choices = ChoiceSerializer(many=True, read_only=True, required=False)

        class Meta:
            model = Poll
            fields = '__all__'
```
### Avec APIView

```
    Creer un fichier apiviews.py
```
```python
    # Importations
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from django.shortcuts import get_object_or_404

    from .models import Poll, Choice
    from  .serializers import PollSerializer

    class PollList(APIView):
        def get(self, request):
            polls = Poll.objects.all()[:20]
            data = PollSerializer(polls, many=True).data
            return Response(data)


    class PollDetail(APIView):
        def get(self, request, pk):
            poll = get_object_or_404(Poll, pk=pk)
            data = PollSerializer(poll).data
            return Response(data)

    # Dans urls.py
    from django.urls import path

    from .apiviews import PollList, PollDetail

    urlpatterns = [
        path("polls/", PollList.as_view(), name="polls_list"),
        path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail")
    ]
```
### Avec Viewset.Model.Viewset

```python
    # Dans le fichier apiviews.py
    from rest_framework import viewsets

    from .models import Poll, Choice
    from .serializers import PollSerializer, ChoiceSerializer


    class PollViewSet(viewsets.ModelViewSet):
        queryset = Poll.objects.all()
        serializer_class = PollSerializer
    
    class ChoiceViewSet(viewsets.ModelViewSet):
        queryset = Choice.objects.all()
        serializer_class = ChoiceSerializer
    
    # Dans le fichier urls.py
    # ...
    from rest_framework.routers import DefaultRouter
    from .apiviews import PollViewSet


    router = DefaultRouter()
    router.register('polls', PollViewSet, base_name='polls')
    router.register('choice', ChoiceViewSet, base_name='choice')


    urlpatterns = [
        # ...
    ]

    urlpatterns += router.urls
```

    NB: -Utilisez viewsets.ModelViewSet lorsque vous allez autoriser toutes les opérations CRUD ou la plupart d'entre elles sur un modèle.
    -Utilisez APIView lorsque vous souhaitez personnaliser complètement le comportement.

### Avec Viewset

```python
    # Dans le fichier apiviews.py
    from rest_framework import viewsets

    from .models import Poll, Choice
    from .serializers import PollSerializer, ChoiceSerializer
    from rest_framework.response import Response

    class PollViewSet(viewsets.ViewSet):
        """
        A simple ViewSet for listing or retrieving Polls.
        """
        def list(self, request):
            queryset = Poll.objects.all()
            serializer = PollSerializer(queryset, many=True)
            return Response(serializer.data)
    
    # Dans le fichier urls.py
    # ...
    from rest_framework.routers import DefaultRouter
    from .apiviews import PollViewSet


    router = DefaultRouter()
    router.register('polls', PollViewSet, base_name='polls')


    urlpatterns = [
        # ...
    ]

    urlpatterns += router.urls
```
