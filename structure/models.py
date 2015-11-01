from django.db import models

# Create your models here.

class Domaine(models.Model):
	domains = (
			("Info","Sciences Informatiques"),
			("Ges","Sciences Administratives"),
			("Comp","Sciences Comptable")

		)
	nomDomaine = models.CharField(max_length=10,choices=domains)
	def __str__(self):
		return self.nomDomaine


class Niveau(models.Model):
	nomNiveau = models.CharField(max_length=50,unique=True)
	domaine = models.ForeignKey('Domaine')
	def __str__(self):
		return self.nomNiveau+","+self.domaine

class Anneeacademique(models.Model):
	debutAnnee = models.IntegerField()
	finAnnee = models.IntegerField()
	chxActuel = (
			("1","Annee Actuelle"),
			("0","Annee Passee"),
		)
	estActuel = models.CharField(max_length=5,choices=chxActuel)
	def __str__(self):
		return self.debutAnnee+"/"+self.finAnnee


class Promotion(models.Model):
	niveau = models.ForeignKey('Niveau')
	anneeacademique = models.ForeignKey('Anneeacademique')
	def __str__(self):
		return self.niveau+":"+self.anneeacademique


class Etudiant(models.Model):
	nom =  models.CharField(max_length=50)
	prenom =  models.CharField(max_length=50)
	email = models.EmailField(max_length=254,unique=True)
	telephone = models.CharField(max_length=15,unique=True)
	promotion = models.ManyToManyField(Promotion)

	def __str__(self):
		return self.prenom+" "+self.nom


class Professeur(models.Model):
	nom =  models.CharField(max_length=50)
	prenom =  models.CharField(max_length=50)
	email = models.EmailField(max_length=254,unique=True)
	telephone = models.CharField(max_length=15,unique=True)
	promotion = models.ManyToManyField(Promotion)

	def __str__(self):
		return self.prenom+" "+self.nom


class Matiere(models.Model):
	nomMatiere = models.CharField(max_length=50)


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
	matiere = models.ForeignKey('Matiere')
	professeur = models.ForeignKey('Professeur')
	promotion = models.ForeignKey('Promotion')


class Salle(models.Model):
	nomSalle = models.CharField(max_length=15)
	promotion = models.ManyToManyField(Promotion)
	def __str__(self):
		return self.nomSalle