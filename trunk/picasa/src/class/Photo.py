# -*- coding: iso-8859-15 -*-

# Représentation d'une photo pour l'application tp picasa
class Photo:
        """ Une photo est représenté avec éventuellement un nom
            et le chemin de la photo sur le disque """

        # Initialise une photo avec son nom et un chemin d'accès sur le disque
        # @param nom : le nom de la photo
        # @param chemin : le chemin d'accès sur le disque
        def __init__(self, nom, chemin, titre):
                self.nom = nom
		self.titre = titre
                self.chemin = chemin

        # retourne le nom de la photo   
        # @return le nom de la photo
        def getNom (self):
                return self.nom

        # retourne le titre de la photo   
        # @return le titre de la photo
        def getTitre (self):
                return self.titre

        #retourne le chemin de l'image
        # @return le chemin d'accès sur le disque de la photo à partir des "lanceurs"
        def getChemin (self):
                return self.chemin
        
        # changement du chemin d'accès aux images (nom du dossier uniquement)
        # @param ancienNom: l'ancien nom du repertoire
        # @param nom: le nouveau nom du dossier
        def changerChemin(self, ancienNom, nom):
            self.chemin = self.chemin.replace(ancienNom, nom)
