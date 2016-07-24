from django.contrib import admin

from .models import Note
# Register your models here.
class detailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'priority', 'course', 'dateEnd')
    list_editable = ('state',)
    list_filter = ('course', 'state')

admin.site.register(Note, detailsAdmin)
