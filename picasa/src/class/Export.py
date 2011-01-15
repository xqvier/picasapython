#!/usr/bin/python

import sys
import os
from Albums import Albums
from Album import Album
from Photo import Photo

class export :
    
    def __init__(self):
        self = self
    
    def exportAlbums(self,albums,titre):    
        indexAlbums = open('../data/mesAlbums/index.html','w')
        indexAlbums.write("<HTML><HEAD><TITLE>"+titre+"HTML</TITLE></HEAD>")
        indexAlbums.write("<BODY style='background-color:red'>")
        indexAlbums.write("<H1>"+titre+"</H1>")    
        indexAlbums.write("Bienvenue dans le monde de HTML.")
        indexAlbums.write("Ceci est un paragraphe.<P>")
        indexAlbums.write("Et ceci est le second.<P>")
        indexAlbums.write("</BODY></HTML>")
        indexAlbums.write("ceci est le fichier index de l'albums")
        indexAlbums.close()
    
    def exportAlbum(self,album):    
        self=self
        
    def crationIndexAlbum(self,album):
        print album.getChemin()
 
    def creationIndexPhoto(self,photo):
        print photo.getChemin()
        
    def cprep(self,dest):
        src = "../data/mesAlbums/"
        if src == dest:
            raise ValueError("Impossible d'exporter: fichier source = fichier destination")

        if not os.path.isdir(src):
            raise ValueError("Le dossier source n'existe pas  "+src)
        
        if not os.path.isdir(dest):
            try:
                os.makedirs(dest)
            except WindowsError, e:
                raise ValueError("Impossible de creer ou de modifier le dossier destination")

             
        src = os.path.abspath(src)
        dest = os.path.abspath(dest)
                            
        for file in os.listdir(src):
            s="%s/%s" % (src,file)
            d="%s/%s" % (dest,file)
            if os.path.isfile(s):
                self.fcopy(s,d)
            elif os.path.isdir(s):
                self.cprep(s,d)
                
    
    def fcopy(self,src, dest):
        fs=open(src,"r")
        fd=open(dest,"w")
    
        for line in fs:
            fd.write(line)
    
        fs.close()
        fd.close()
    


try:
    albums = Albums()
    p = export()
    p.exportAlbums(albums,'Tous mes albums PICASSA')
    #p.cprep("C:\Users\Silou\Desktop\Test_Copy_pyton")
except ValueError, e:
    print e.args


sys.exit(0)
