# -*- coding: iso-8859-15 -*-
import os
import re
import urllib2
import urllib
from Photo import Photo

# Représentation d'un album pour l'application tp picasa
class Album:
        """ un album est représenté par un nom, l'url qui a permis l'acquisition des images 
                ( pour permettre la synchronisation éventuelle???), une liste des images miniatures
                et une liste des images taille réelle """

        # initialise un album de photo avec son url et un nom
        # @param nom : le nom de l'album a créer (unicité vérifié)
        # @param url : l'url des images a synchroniser
        def __init__(self,nom, url):
                self.nom = nom
                self.url = url
                self.listMiniature = list()
                self.listGrande = list()
                self.synchronisation()
                
        # recuperation des données à partir de l'url utilisé lors de l'initialisation
        # permet la resynchronisation
        def synchronisation(self):
                chaine = urllib2.urlopen(self.url).read()
                # decoupage pour conserver uniquement ce qui se trouve entre les balise <noscript> et </noscript>
                chaine = chaine.split("lhid_feedview")
                chaine = chaine[1].split("<noscript>")
                chaine = chaine[1].rsplit("</noscript>")
                
                # recuperation des liens des images miniatures
                regex = "src=\"{1}(\S*|\s*)\">{1}"
                pattern = re.compile(regex)
                liensImagesMiniatures = re.findall(pattern, chaine[0])
                
                # recuperation des liens des images taille réelle
                liensImagesGrande = list(liensImagesMiniatures)
                for i in range(0,len(liensImagesGrande)):
                        liensImagesGrande[i] = re.sub("/s128/", "/", liensImagesGrande[i])
        
                # recuperation des titres des images
                regex = "<p><a\ href=\"\S*\"(>.*?<)/a></p>"
                #re.DOTALL très important pour les titres sur plusieurs lignes
                pattern = re.compile(regex, re.DOTALL)
                titres = re.findall(pattern, chaine[0])

                #traitement pour enlever le caractere parasite qui sert a garder le bon ordre des titres
                for i in range(0, len(titres)):
                        titres[i] = titres[i][1:] 
                
                # enregistrement des images sur le disque
                for i in range(0, len(liensImagesMiniatures)):
                        #petite
                        obj = liensImagesMiniatures[i].split("/")                       
                        self.listMiniature.append(Photo(obj[len(obj)-1],"./data/mesAlbums/"+self.nom+"/minis/"+obj[len(obj)-1], titres[i]))
                        urllib.urlretrieve(liensImagesMiniatures[i], "./data/mesAlbums/"+self.nom+"/minis/"+obj[len(obj)-1])
                        #grandes
                        obj = liensImagesGrande[i].split("/")
                        self.listGrande.append(Photo(obj[len(obj)-1], "./data/mesAlbums/"+self.nom+"/grandes/"+obj[len(obj)-1], titres[i]))
                        #self.listGrande.append(Photo('',"./data/mesAlbums/"+self.nom+"/grandes/"+obj[len(obj)-1] ))
                        urllib.urlretrieve(liensImagesGrande[i], "./data/mesAlbums/"+self.nom+"/grandes/"+obj[len(obj)-1])
                
                
        # retourne le nom de l'album    
        # @return le nom de l'album
        def getNom(self):
                return self.nom     

        #retourne l'url d'acquisition de l'album
        # @return l'url d'acquisition des images de l'album
        def getUrl(self):
                return self.url
        
        #retourne une liste de photos miniatures
        # @return la liste des photos miniatures de l'album
        def getListeMiniatures(self):
                return self.listMiniature
        
        #retourne une liste de photos taille réelle
        # @return la liste des photos taille réelle de l'album
        def getListeGrandes(self):
                return self.listGrande
        
        #renomme l'album avec un nouveau nom
        # @param nom : le nouveau nom de l'album
        def renommer(self, nom):
         
                # on modifie les chemins des images
                for x in self.listMiniature:
                    x.changerChemin(self.nom, nom)
                        
                for x in self.listGrande:
                    x.changerChemin(self.nom, nom)
                        
                # renommage du dossier de l'album
                os.rename("./data/mesAlbums/"+self.nom, "./data/mesAlbums/"+nom)
                
                # on modifie le nom de l'album
                self.nom = nom
                
