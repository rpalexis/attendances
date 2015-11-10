from django.db import models

# Create your models here.

class Domaine(models.Model):
	domains = (
			("Info","Sciences Informatiques"),
			("Ges","Sciences Administratives"),
			("Comp","Sciences Comptable")

		)
	nomDomaine = models.CharField(max_length=10,choices=domains, verbose_name= 'Nom du Domaine')
	def __str__(self):
		return self.nomDomaine
	class Meta:
		verbose_name = "Domaine"
		verbose_name_plural = "Domaines"


class Niveau(models.Model):
	nomNiveau = models.CharField(max_length=50,unique=True, verbose_name='Niveau')
	domaine = models.ForeignKey('Domaine')
	def __str__(self):
		return self.nomNiveau+","+self.domaine.nomDomaine

	class Meta:
		verbose_name = "Niveau"
		verbose_name_plural = "Niveaux"

class Anneeacademique(models.Model):
	debutAnnee = models.IntegerField()
	finAnnee = models.IntegerField()
	chxActuel = (
			("1","Annee Actuelle"),
			("0","Annee Passee"),
		)
	#estActuel = models.CharField(max_length=5,choices=chxActuel)
	estActuel = models.BooleanField()
	def __str__(self):
		return str(self.debutAnnee)+"/"+str(self.finAnnee)

	class Meta:
		verbose_name = "Annee Academique"
		verbose_name_plural = "Annees Academiques"


class Promotion(models.Model):
	niveau = models.ForeignKey('Niveau')
	anneeacademique = models.ForeignKey('Anneeacademique')
	def __str__(self):
		return self.niveau.nomNiveau+":"+str(self.anneeacademique.debutAnnee)+"/"+str(self.anneeacademique.finAnnee)

	class Meta:
		verbose_name = "Promotion"
		verbose_name_plural = "Promotions"


class Etudiant(models.Model):
	nom =  models.CharField(max_length=50)
	prenom =  models.CharField(max_length=50)
	email = models.EmailField(max_length=254,unique=True)
	telephone = models.CharField(max_length=15,unique=True)

	def __str__(self):
		return self.prenom+" "+self.nom

	class Meta:
		verbose_name = "Etudiant"
		verbose_name_plural = "Etudiants"


class Appartenance(models.Model):
	etudiant =  models.ForeignKey('Etudiant')
	promotion = models.ForeignKey('Promotion')
	

class Professeur(models.Model):
	nom =  models.CharField(max_length=50)
	prenom =  models.CharField(max_length=50)
	email = models.EmailField(max_length=254,unique=True)
	telephone = models.CharField(max_length=15,unique=True)

	def __str__(self):
		return self.prenom+" "+self.nom

	class Meta:
		verbose_name = "Professeur"
		verbose_name_plural = "Professeurs"


class Matiere(models.Model):
	nomMatiere = models.CharField(max_length=50)
	def __str__(self):
		return self.nomMatiere

	class Meta:
		verbose_name = "Matiere"
		verbose_name_plural = "Matieres"
class Horaire(models.Model):
	#(jourMatiere,Matieres,professeur,promotion)
	jour = (
			("1","Lundi"),
			("2","Mardi"),
			("3","Mercredi"),
			("4","Jeudi"),
			("5","Vendredi"),
			("6","Samedi"),
			("7","Dimanche"),
		)
	jourMatiere = models.CharField(max_length=5,choices=jour)
	heureDebut = models.TimeField(auto_now=False, auto_now_add=False)
	heureFin = models.TimeField(auto_now=False, auto_now_add=False)
	matiere = models.ForeignKey('Matiere')
	professeur = models.ForeignKey('Professeur')
	promotion = models.ForeignKey('Promotion')

	class Meta:
		verbose_name = "Horaire"
		verbose_name_plural = "Horaires"

class Salle(models.Model):
	nomSalle = models.CharField(max_length=15)
	def __str__(self):
		return self.nomSalle

	class Meta:
		verbose_name = "Salle"
		verbose_name_plural = "Salles"

class UsageSalle(models.Model):
	salle = models.ForeignKey('Salle')
	promotion = models.ForeignKey('Promotion')

	def __str__(self):
		return self.salle.nomSalle

	class Meta:
		verbose_name = "Utilisation des Salles"
		verbose_name_plural = "Utilisation des Salles"