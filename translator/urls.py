from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover, name='cover'),
    path('translator<int:alg_id>', views.translator, name='translator'),
    path('translated<int:alg_id>', views.translated, name='translated'),

]
