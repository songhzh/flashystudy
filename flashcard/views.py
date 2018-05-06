from django.shortcuts import render
from django.views import generic
from .models import Deck, Card

class IndexView(generic.ListView):
    model = Deck
    template_name = 'flashcard/index.html'
    context_object_name = 'deck_list'

class StudyView(generic.DetailView):
    model = Deck
    template_name = 'flashcard/study.html'