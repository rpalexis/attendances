from django.contrib import admin
from structure.models import *

# Register your models here.

class DomainAdmin(admin.ModelAdmin):
	list_display = ('nomDomaine',)


class NiveauAdmin(admin.ModelAdmin):
	list_display = ('nomNiveau','domaine',)


class AnneeacademiqueAdmin(admin.ModelAdmin):
	list_display = ('debutAnnee','finAnnee',)


class PromotionAdmin(admin.ModelAdmin):
	pass


class EtudiantAdmin(admin.ModelAdmin):
	pass


class ProfesseurAdmin(admin.ModelAdmin):
	pass


class MatiereAdmin(admin.ModelAdmin):
	pass


class HoraireAdmin(admin.ModelAdmin):
	pass


class SalleAdmin(admin.ModelAdmin):
	pass

class UsageSalleAdmin(admin.ModelAdmin):
	pass


class AppartenanceAdmin(admin.ModelAdmin):
	pass


admin.site.register(Domaine,DomainAdmin)
admin.site.register(Niveau,NiveauAdmin)
admin.site.register(Anneeacademique,AnneeacademiqueAdmin)
admin.site.register(Promotion,PromotionAdmin)
admin.site.register(Etudiant,EtudiantAdmin)
admin.site.register(Professeur,ProfesseurAdmin)
admin.site.register(Matiere,MatiereAdmin)
admin.site.register(Horaire,HoraireAdmin)
admin.site.register(Salle,SalleAdmin)
admin.site.register(UsageSalle,UsageSalleAdmin)
admin.site.register(Appartenance,AppartenanceAdmin)