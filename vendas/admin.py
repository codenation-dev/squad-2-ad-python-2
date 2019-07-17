from django.contrib import admin

# Register your models here.
from .models import Venda


class VendasAdmin(admin.ModelAdmin):
    list_display = ("mes", "id_vendedor")


admin.site.register(Venda, VendasAdmin)
