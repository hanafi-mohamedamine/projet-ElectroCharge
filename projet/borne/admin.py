from django.contrib import admin
from .models import Borne, TypeConnecteur, SessionCharge


@admin.register(Borne)
class BorneAdmin(admin.ModelAdmin):
    list_display = ('identifiant', 'emplacement', 'puissance_kw', 'statut', 'date_installation', 'connecteur')
    list_filter = ('statut', 'connecteur')
    search_fields = ('identifiant', 'emplacement')


@admin.register(TypeConnecteur)
class TypeConnecteurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'vitesse_charge')
    

@admin.register(SessionCharge)
class SessionChargeAdmin(admin.ModelAdmin):
    list_display = ('borne', 'date_debut', 'duree_minutes', 'energie_kwh')

    