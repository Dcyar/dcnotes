from django.conf.urls import url
from django.contrib import admin

from apps.notes.views import IndexView, NoteForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name = 'index'),
    url(r'^notes/(?P<note>[\w\-]+)$', IndexView.as_view(), name = 'index'),
    url(r'^newnote$', NoteForm.as_view(), name = 'new_note'),

    url(r'^cambiarEstado/(\d+)$', 'apps.notes.views.cambiarEstado', name='cambiarEstado'),
]
