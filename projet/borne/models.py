from django.db import models

class TypeConnecteur(models.Model):
    nom = models.CharField(max_length=50)

    VITESSE_CHOICES = [
        ('rapide', 'Rapide'),
        ('standard', 'Standard'),
    ]

    vitesse_charge = models.CharField(max_length=20,choices=VITESSE_CHOICES)

    def __str__(self):
        return self.nom

class Borne(models.Model):
    STATUT_CHOICES = [
        ('libre', 'Libre'),
        ('occupee', 'Occupée'),
        ('maintenance', 'En maintenance'),
    ]

    identifiant = models.CharField(max_length=100, unique=True)
    emplacement = models.CharField(max_length=100)
    puissance_kw = models.FloatField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    date_installation = models.DateField()
    connecteur = models.ForeignKey(TypeConnecteur, on_delete=models.CASCADE)

    def __str__(self):
        return self.identifiant
    

class SessionCharge(models.Model):
    borne = models.ForeignKey(Borne, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    duree_minutes = models.IntegerField()
    energie_kwh = models.FloatField()

    def __str__(self):
        return f"Session - {self.borne.identifiant}"
