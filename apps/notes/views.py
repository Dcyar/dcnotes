from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.notes.forms import NoteForm
from .models import Note
# Create your views here.

class IndexView(ListView):
    model = Note
    template_name = 'index.html'
    context_object_name = 'notes'

    def get_queryset(self):
        if self.kwargs.get('note'):
            queryset = self.model.objects.filter(slug=self.kwargs['note'])
        else:
            queryset = super(IndexView, self).get_queryset()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context


class NoteForm(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_form.html'
    success_url = reverse_lazy('index')


def cambiarEstado(request, id_nota):
    note = Note.objects.get(pk = id_nota)
    note.state = True
    note.save()

    return HttpResponseRedirect("/", locals())
