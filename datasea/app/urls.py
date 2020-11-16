from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('now', views.now, name='now'),
    path('api', views.api, name='now'),
    path('market', views.market, name='market'),
]
