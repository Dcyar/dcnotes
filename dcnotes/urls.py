from django.conf.urls import url
from django.contrib import admin

from apps.notes.views import IndexView, NoteDetailView, NoteForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name = 'index'),
    url(r'^note/(?P<slug>[\w\-]+)$', NoteDetailView.as_view(), name = 'noteDetail'),
    url(r'^newnote$', NoteForm.as_view(), name = 'new_note'),

    url(r'^cambiarEstado/(\d+)$', 'apps.notes.views.cambiarEstadoIndex', name='cambiarEstadoIndex'),
    url(r'^cambiarEstadoDetail/(\d+)$', 'apps.notes.views.cambiarEstadoDetail', name='cambiarEstadoDetail'),
]
