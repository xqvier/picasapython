#!/usr/bin/python

import sys
sys.path.append('./class')

from Albums import Albums


#Verification de la syntaxe de la ligne de commande
if len(sys.argv) < 3 or (sys.argv[1] == "import" or sys.argv[1] == "rename")) and len(sys.argv) < 4):
    print "Erreure de syntaxe"
    print "Usage : %s action albumName [url|newName]" % (sys.argv[0])
    print "\taction :" 
    print "\t\timport - Importe un album depuis picasaweb et prend l'url en 4eme argument."
    print "\t\tdel - Efface l'album dont le nom est spécifié par albumName"
    print "\t\trename - Renomme le repertoire dont le nom courant est albumName et le nouveau nom est newName"
    print "\t\tsynchronize - Synchronise l'album identifié par albumName pour mettre a jour les nouvelles photo et supprimer les photos qui n'existe plus d'un album déja importé"

action = sys.argv[1]
albumName = sys.argv[2]

if(action == "import"):
    url = sys.argv[3]
    try :
        print "Importation de l'album en cours..."
        Albums.ajouterAlbum(albumName,url)
    except ValueError:
        print "Ce nom d'album est deja pris ou cette url est deja synchronisee"
        
if(action == "del"):
    try:
        print "Effacement de l'album en cours..."
        Albums.retraitAlbum(albumName)
    except ValueError:
        print "Cet album n'existe pas, verifiez le nom de l'album"
        
if(action == "rename"):
    newName = sys.argv[3]
    try:
        print "Renommage de l'album en cours..."
        Albums.renommerAlbum(albumName, newName)
    except ValueError:
        print "Cet album n'existe pas ou le nom est deja pris"
        
if(action == "synchronize"):
    try:
        print "Synchronisation de l'album en cours..."
        Albums.sync(albumName)
    except ValueError:
        print "Cet album n'existe pas"



sys.exit(0);        
