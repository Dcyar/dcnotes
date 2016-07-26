from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages

from apps.notes.forms import NoteForm
from .models import Note
# Create your views here.

class IndexView(ListView):
    model = Note
    template_name = 'index.html'
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'
    context_object_name = 'note'

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)

        return context


class NoteForm(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_form.html'
    success_url = reverse_lazy('index')


def cambiarEstadoIndex(request, id_nota):
    note = Note.objects.get(pk = id_nota)
    note.state = True
    note.save()
    messages.success(request, "Estado cambiado satisfactoriamente", extra_tags = 'center-align col s11')

    return HttpResponseRedirect("/", locals())

def cambiarEstadoDetail(request, id_nota):
    note = Note.objects.get(pk = id_nota)
    note.state = True
    note.save()
    messages.success(request, "Estado cambiado satisfactoriamente", extra_tags = 'center-align col s11')

    return HttpResponseRedirect("/note/" + note.slug, locals())
