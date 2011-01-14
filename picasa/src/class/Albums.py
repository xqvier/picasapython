# -*- coding: iso-8859-15 -*-
from Album import Album
import pickle
import os.path
import shutil

# Représentation de la liste des albums gérés
class Albums:
        """ La liste des albums gérés par l'application """
                # chemin du fichier de sauvegarde des données
        cheminFichier = './data/albums.dat'             
                
        # initialise la collection d'albums avec le précédent contenu s'il existe
        def __init__(self):
                self.albums = list()
                self.charger()
        
        # sauvegarde de l'état de l'album dans un fichier
        def sauvegarder(self):
                fichier = open(Albums.cheminFichier, "w")
                pickle.dump(self.albums, fichier)
                fichier.close()

        # charger l'album dans l'état de sauvegarde précédent
        def charger(self):
                if(os.path.isfile(Albums.cheminFichier)):
                    fichier = open(Albums.cheminFichier, "r")
                    self.albums = pickle.load(fichier)
                    fichier.close()
        
        # ajout d'un album a la collection déjà existante
                # @param nom : le nom a donner à l'album
                # @param url : l'url du la page de l'album
                # @exception : ValueError si le nom de l'album existe déjà (de nom) ou si l'album est déjà syncrhonisé( d'url)
        def ajouterAlbum(self, nom, url):
                # on vérifie que l'album n'est pas déjà présent soit par le nom soit par l'url
                i = 0
                while((i < len(self.albums)) and self.albums[i].getNom().lower() != nom.lower() and self.albums[i].getUrl().lower() != url.lower()):
                     	i += 1
                                   
                if(i != len(self.albums)):
                    raise ValueError("Album déjà présent")
                                   
                # creation de l'arborescence
                os.mkdir('./data/mesAlbums/' + nom)
                os.mkdir('./data/mesAlbums/' + nom + '/grandes')
                os.mkdir('./data/mesAlbums/' + nom + '/minis')
                # création de l'album
                self.albums.append(Album(nom, url))
                                   
                #sauvegarde des modifications
                self.sauvegarder()

        
        # synchronisation d'un album à l'aide de son nom
                # @param nom : le nom de l'album a resynchroniser
                # @exception : ValueError si le nom de l'album n'existe pas
        def sync(self, nom):
                #on cherche l'album a resynchroniser
                i = 0
                while((i < len(self.albums)) and self.albums[i].getNom().lower() != nom.lower()):
                        i += 1
                
                if(i == len(self.albums)):
                        raise ValueError("Album " + nom + " non présent")
                
                # on resynchronise l'album
                self.albums[i].synchronisation()
                
                #sauvegarde des modifications
                self.sauvegarder()
                
        # retrait d'un album de la collection à l'aide de son nom
                # @param nom : le nom de l'album a retirer
                # @exception : ValueError si le nom de l'album n'existe pas
        def retraitAlbum(self, nom):
                #on cherche l'album a retirer
                i = 0
                while((i < len(self.albums)) and self.albums[i].getNom().lower() != nom.lower()):
                        i += 1
                
                if(i == len(self.albums)):
                        raise ValueError("Album " + nom + " non présent")
                        
                # suppresion de l'arborescence
                shutil.rmtree('./data/mesAlbums/' + self.albums[i].getNom())
                # suppression de la liste
                self.albums.remove(self.albums[i])
                
                #sauvegarde des modifications
                self.sauvegarder()
                
                # retourne tous les albums de l'utilisateur
                # @return les albums de l'utilisateur
        def getAlbums(self):
                return self.albums
                
        # renomme un album
        # @param nom : le nom actuel de l'album
        # @param nouveauNom : le nouveau nom à donner à l'album
        # @exception : ValueError si le nom de l'album n'existe pas ou si le nom est déjà pris
        def renommerAlbum(self, nom, nouveauNom):
                #on cherche l'album a resynchroniser
                i = 0
                while((i < len(self.albums)) and self.albums[i].getNom().lower() != nom.lower()):
                        i += 1
                        
                if(i == len(self.albums)):
                        raise ValueError("Album " + nom + " non présent")
                        
                #on vérifie qu'un album ne porte pas le nouveauNom
                x = 0
                while((x < len(self.albums)) and self.albums[x].getNom().lower() != nouveauNom.lower()):
                        x += 1
                        
                if(x != len(self.albums)):
                        raise ValueError("Album " + nouveauNom + " déjà existant")
                        
                #on peut renommer l'album
                self.albums[i].renommer(nouveauNom)
                
                # sauvegarde des modifications
                self.sauvegarder()

