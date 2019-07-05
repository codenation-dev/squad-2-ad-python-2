from django.contrib import admin

# Register your models here.
from .models import PlanoComissoes


class VendasAdmin(admin.ModelAdmin):
    list_display = ("descricao", "valor_minimo", "percent_min", "percent_max")


admin.site.register(PlanoComissoes)
