from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from .models import Deck, Card
from .forms import NewDeckForm


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

def new_deck(request):
    if request.method == 'POST':
        form = NewDeckForm(request.POST)
        if form.is_valid():
            deck_name = request.POST.get('deck_name')
            if Deck.objects.filter(deck_name__iexact=deck_name):
                messages.error(request, 'A deck with that name already exists.')
            else:
                form.save()
                return redirect(reverse('flashcard:index'))
        else:
            messages.error(request, 'You must enter a deck name.')
        return redirect(reverse('flashcard:select'))
    else:
        form = NewDeckForm()
    return render(request, 'flashcard/select.html', {'form': form})
