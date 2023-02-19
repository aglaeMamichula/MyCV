from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('results/', views.results, name='results'),
    path('vote/', views.vote, name='vote'),
]