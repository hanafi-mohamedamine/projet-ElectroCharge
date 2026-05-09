from django.shortcuts import  render
from .models import Borne, TypeConnecteur, SessionCharge


def liste_bornes(request):
    bornes = Borne.objects.all()

    statut = request.GET.get('statut')
    puissance = request.GET.get('puissance')
    connecteur = request.GET.get('connecteur')
    ville = request.GET.get('ville')

    if statut:
        bornes = bornes.filter(statut=statut)

    if puissance:
        bornes = bornes.filter(puissance_kw=puissance)

    if ville:
        bornes = bornes.filter(emplacement=ville)

    if connecteur:
        bornes = bornes.filter(connecteur_id=connecteur)


    context = {
        'bornes': bornes,
        'connecteurs': TypeConnecteur.objects.all(),
        'puissances': Borne.objects.values_list('puissance_kw', flat=True).distinct(),
        'villes' : Borne.objects.values_list('emplacement', flat=True).distinct()
    }

    return render(request, 'borne/liste.html', context)


def sessions(request):
    sessions = SessionCharge.objects.all()
    return render(request, 'borne/sessions.html', {'sessions': sessions} )

def connecteur(request):
    connecteurs = TypeConnecteur.objects.all()
    return render(request, 'borne/connecteur.html', {'connecteurs': connecteurs} )


def home(request):
    return render(request, 'borne/home.html')










    
