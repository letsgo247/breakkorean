from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover, name='cover'),
    path('translator1', views.translator1, name='translator1'),
    path('translator2', views.translator2, name='translator2'),
    path('translator3', views.translator3, name='translator3'),
    path('translated1', views.translated1, name='translated1'),
    path('translated2', views.translated2, name='translated2'),
    path('translated3', views.translated3, name='translated3'),

]
