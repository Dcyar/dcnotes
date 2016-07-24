from django import forms

from apps.notes.models import Note

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note

        fields = [
                'title',
                'description',
                'priority',
                'dateEnd',
                'course'
        ]
        labels = {
                'title': 'Título de la nota',
                'description' : 'Descripción',
                'priority' : 'Prioridad',
                'dateEnd' : 'Fecha de entrega',
                'course' : 'Curso'
        }
        widgets = {
                'title': forms.TextInput(attrs={'class':'validate'}),
                'description' : forms.Textarea(attrs={'class':'validate materialize-textarea'}),
                'priority' : forms.NumberInput(attrs={'class':'validate'}),
                'dateEnd' : forms.DateInput(attrs={'type':'date','class':'datepicker'}),
                'course' : forms.Select(attrs={'class':'validate browser-default'})
        }
