#!/usr/bin/python

import sys
sys.path.append('./class')

from Albums import Albums


#Verification de la syntaxe de la ligne de commande
if len(sys.argv) < 3 or ((sys.argv[1].lower() == "import" or sys.argv[1].lower() == "rename") and len(sys.argv) < 4):
    print "Erreure de syntaxe"
    print "Usage : %s action albumName [url|newName]" % (sys.argv[0])
    print "action :" 
    print "\timport - Importe un album depuis picasaweb et prend l'url en 4eme argument."
    print "\tdel - Efface l'album dont le nom est specifie par albumName"
    print "\trename - Renomme le repertoire dont le nom courant est albumName et le nouveau nom est newName"
    print "\tsync - Synchronise l'album identifie par albumName pour mettre a jour les nouvelles photo et supprimer les photos qui n'existe plus d'un album deja importe"
    print "albumName : Le nom de l'album concerne"
    print "url : l'url d'importation de l'album"
    print "newName : Le nouveau nom de l'album dans le cadre d'un renommage"
    sys.exit(1)
    
action = sys.argv[1].lower()
albumName = sys.argv[2].lower()

albums = Albums();

if(action == "import"):
    url = sys.argv[3]
    try :
        print "Importation de l'album en cours..."
        albums.ajouterAlbum(albumName,url)
        print "Importation terminee"
    except ValueError:
        print "Ce nom d'album est deja pris ou cette url est deja synchronisee"
        
if(action == "del"):
    try:
        print "Effacement de l'album en cours..."
        albums.retraitAlbum(albumName)
        print "Effacement termine"
    except ValueError:
        print "Cet album n'existe pas, verifiez le nom de l'album"
        
if(action == "rename"):
    newName = sys.argv[3]
    try:
        print "Renommage de l'album en cours..."
        albums.renommerAlbum(albumName, newName)
        print "Renommage termine"
    except ValueError:
        print "Cet album n'existe pas ou le nom est deja pris"
        
if(action == "sync"):
    try:
        print "Synchronisation de l'album en cours..."
        albums.sync(albumName)
        print "Synchronisation termine"
    except ValueError:
        print "Cet album n'existe pas"



sys.exit(0);        
