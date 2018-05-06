from django.urls import path
from . import views

app_name = 'flashcard'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StudyView.as_view(), name='study'),
]
