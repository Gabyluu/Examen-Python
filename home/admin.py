from django.contrib import admin

# Register your models here.
from .models import Archivos_Investigacion


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'autor','categoria')
	search_fields = ('titulo', 'autor')
	list_filter = ('categoria',)

admin.site.register(Archivos_Investigacion, AuthorAdmin)

