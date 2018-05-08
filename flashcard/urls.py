from django.urls import path
from . import views

app_name = 'flashcard'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('select/', views.SelectView.as_view(), name='select'),
    path('create/<int:pk>/', views.CreateView.as_view(), name='create'),
    path('study/<int:pk>/', views.StudyView.as_view(), name='study'),
    path('newdeck/', views.new_deck, name='newdeck'),
    path('deldeck/', views.del_deck, name='deldeck'),
]