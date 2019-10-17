from django.urls import path
from . import views, andviews

urlpatterns = [
    path('', views.cover, name='cover'),
    path('select', views.select, name='select'),
    path('translator<int:alg_id>', views.translator, name='translator'),
    path('translated<int:alg_id>', views.translated, name='translated'),

    path('and', andviews.cover, name='andcover'),
    path('andselect', andviews.select, name='andselect'),
    path('andtranslator<int:alg_id>', andviews.translator, name='andtranslator'),
    path('andtranslated<int:alg_id>', andviews.translated, name='andtranslated'),

]
