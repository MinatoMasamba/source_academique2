from django.contrib import admin
from .models import Cours, Interro, Examen, TP, Note

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('titre', 'promotion')

admin.site.register(Interro)
admin.site.register(Examen)
admin.site.register(TP)
admin.site.register(Note)
