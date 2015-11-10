
Cahier des charges
Nom du systeme : Gestion Presences professeurs et la dispensation des cours a ESIH

Il s'agit de concevoir un systeme informatique qui va faciliter le controle de la regularite des professeurs.
Ce systeme compte prendre en compte l'existant a savoir l'actuel de faire. Et ajouter d'autres fonctionnalites

Parmis les fonctionnalites proposees:

	-> Gestion des salles de classe
	-> Gestion des promotions(Avec des entites faibles telles: Info Gestion| Comptabilite)
	-> Gestion des matieres (Et leurs contenus)
	-> Gestion des horaires
	-> Gestion des professeurs
	-> Gestion des etudiants



	Le professeur devrait etre capable de:
		-> Communiquer avec ses etudiants:
					[]* Avertir d'un retard
					[]* Publier le contenu du prochain cours
					[]* Publier le programme de son cours 
		-> Confirmer sa presence a un cours (Avec un code)

	Les etudiants devraient etre capable de:
		-> Consulter son horaire
		-> Confirmer sa participation a un cours(l'evaluer)
		-> Recevoir des notifications concernant un cours (par email ou par sms)
		-> S'incrire dans une promotion

	Le responsables des presences devrait etre capable de:
		-> Modifier le lieu pour la tenue d'un cour
		-> Avoir acces a un resume de l'etat actuel des cours
		-> Produire des rapports bases sur la presence de chaque professeurs
		-> Controler l'evolution du programme de chaque matiere
		-> Faire des CRUD sur les diferents entites

==============================================================================================================================
PRESENTATION DES ENTITES & RELATIONS
==============================================================================================================================
		[] SALLES
			(nomSalle) #On prend uniquement le nom de la salle(salle physique) Ex: Salle7 ect
		[] AnneeAcademique
			(debutAnnee,finAnnee,current)#a boolean to know the current academic's year
		[] Domaine # Prendre en compte les domaines disponible a l'ecole# (Info, Gestion, Comptabilite, Genie)
			(nomDomaine)
		[] Niveau
			(nomNiveau)
		[] Matieres
			(nomMatiere)#Entite en relation avec Horaire
		[] Professeurs
			(nom,prenom,email,telephone1,telephone2)#Entite en relation avec Horaire
		[] Horaire
			(jourMatiere,Matieres,professeur,promotion)
		[] Etudiant 
			(nom,prenom,email,telephone1,telephone2,promotion)


		[] Promotion (#Entite creant une liaison entre les entites Niveau et AnneeAcademique)
					  #Les entites Horaires, Etudiant, Salle seront en relation directe avec elle
					  # Ceci pour suivre l'evolution des entites pre-citees a travers les annees academiques




==============================================================================================================================
ISSUES
==============================================================================================================================
[] Fix: Faire en sorte en gerant l'entite Promotion on puisse garder toutes les informations des annees academiques precedentes
[] Help : Mieux definir les entites annee et promotion pour mieux comprendre le concept de classe/salle
[] feat :  L'espace sera consultable par les etudiants rapidement sans trop d'informations a part les informations visant a faire la demande d'un cours.
[] Fix : Mettre jourMatiere disponible en selection dans l'horaire afin d'avoir un integer que l'on puisse gerer avec timeDelta lorsqu'on aura besoin de connaitre les horaires pour un jour donne et pour une promotion donnee
[] Trouble: un etudiant est dans une promotion certe. Mais je n'ai pas encore gerer le probleme de faire la reference a une promotion 
en tenant compte des differentes annees academiques.
	[R]:Introduire une table ANNEE_ACADEMIK aiderait. Ce qui aurait une relation avec la table promotion
[] Feat: La presence du professeur sera confirme grace a un mecanisme bizard. la moitie d'un code sera partager entre les professeurs et les etudiants pour s'assurer que les cours ont ete tenue.

==============================================================================================================================
Index Functionnalities
==============================================================================================================================

 --> For the admin
 In the dashboard, see things like:
       Horaire du Jour par promotion
       MSG_SENders
       Link to Add content
       Link to See Horaire par promotion

--> For Students and Prof
		See Their Schedule
		MSG_Senders
