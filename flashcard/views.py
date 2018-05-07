from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Deck, Card


class IndexView(generic.TemplateView):
    template_name = 'flashcard/index.html'

class SelectView(generic.ListView):
    model = Deck
    template_name = 'flashcard/select.html'
    context_object_name = 'deck_list'

class StudyView(generic.DetailView):
    model = Deck
    template_name = 'flashcard/study.html'

class CreateView(generic.TemplateView):
    template_name = 'flashcard/create.html'

def newDeck(request):
    if Deck.objects.filter(deck_name__iexact='math').exists():
        messages.error(request, 'Deck with the same name already exists')
        return redirect('flashcard:select')
    else:
        return
