from django.urls import path

from . import views

urlpatterns = [
    path('html/<str:nome>', views.html, name='html'),
    path('csv/<str:nome>', views.csv, name='csv'),
    path('json/<str:nome>', views.json, name='json'),
]
