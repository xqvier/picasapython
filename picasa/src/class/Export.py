#!/usr/bin/python

import sys
import os
from Albums import Albums
from Album import Album
from Photo import Photo
from wxPython.wx import *

class Export :
    
    def __init__(self):
        self = self
    
    def indexAlbums(self,albums,titre):    

        indexAlbums = open('./data/mesAlbums/index.html','w')
        indexAlbums.write("<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//FR' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>")
        indexAlbums.write("<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='fr' lang='fr'><HEAD><meta http-equiv='Content-Type' content='text/html; charset=utf-8' />")
        indexAlbums.write("<TITLE>"+titre+"HTML</TITLE></HEAD>")
        indexAlbums.write("<BODY style='background-color:#798073'>")
        indexAlbums.write("<H1 align='center'>"+titre+"</H1>")    
        indexAlbums.write("<TABLE align='center' style='background-color:#FFF'>")
        indexAlbums.write("<tr><td></td></tr><tr>")
        i=0
        libel ="<tr>"
        for album in albums.getAlbums():
            self.indexAlbum(album,titre,true)
            photo = album.getListeMiniatures()[0]
            lien = photo.getChemin()
            img = wxImage(lien)
            nom = album.getNom()
            lien = lien[17:len(lien)].replace('%','%25')
            i = i+1
            width = img.GetWidth()
            height = img.GetHeight()     
            if(height < width ):
                indexAlbums.write("<td align='center' height='140' width='140' style='background-color:#798073' ><a href='"+nom+"/index.html'><img src='"+lien+"' border='0' width='135px' /></a></td>")
                libel = libel + "<td align='center'> <a  href='"+nom+"/index.html'>"+nom +"</a></td>"
            else :
                indexAlbums.write("<td align='center'height='140' width='140' style='background-color:#798073' ><a  href='"+nom+"/index.html'><img src='"+lien+"' border='0' height='130px' /></a></td>")
                libel = libel + "<td align='center'> <a  href='"+nom+"/index.html'>"+nom +"</a></td>"
            if(i%7 == 0):
                libel = libel + "</tr>"
                indexAlbums.write(libel)
                libel ="<tr>"
        if(i%7 != 0):
            libel = libel + "</tr>"
            indexAlbums.write(libel)
            libel ="<tr>"
            #indexAlbums.write("<tr><td style='background-color:#798073'><a href='"+photo[17:len(photo)]+"'>"+photo[17:len(photo)]+" </a></td></tr>")
        indexAlbums.write("</TABLE></BODY></HTML>")
        indexAlbums.close()
    
    
    
    ''' le troisime parametre et true ou false permet qu si on exporte tous les albums d'avoir un lien vers l'index de tous'''
    def indexAlbum(self,album,titre,bool): 
        indexAlbums = open('./data/mesAlbums/'+album.getNom()+'/index.html','w')
        indexAlbums.write("<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//FR' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>")
        indexAlbums.write("<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='fr' lang='fr'><HEAD><meta http-equiv='Content-Type' content='text/html; charset=utf-8' />")
        indexAlbums.write("<TITLE>"+titre+"HTML</TITLE></HEAD>")
        indexAlbums.write("<BODY style='background-color:#798073'>")
        if(bool):
            indexAlbums.write("<H1 align='center'><a href='../index.html'>"+titre+"</a></H1>")   
        indexAlbums.write("<H3 align='center'> Album : "+album.getNom()+"</H3>")    
        indexAlbums.write("<TABLE align='center' style='background-color:#FFF'>")
        indexAlbums.write("<tr><td></td></tr><tr>")
        nbphoto = len(album.getListeMiniatures())
        i=0
        libel ="<tr>"
        for photo in album.getListeMiniatures():
            lien = photo.getChemin()
            img = wxImage(lien)
            nom = photo.getTitre()[0:19].replace('%20',' ').replace('%28',' ').replace('%29',' ').replace('%C3',' ').replace('%A9',' ')
            if(len(nom)<5):
                nom = photo.getNom()[0:25].replace('%20',' ').replace('%28',' ').replace('%29',' ').replace('%C3',' ').replace('%A9',' ');
            lienhtml = photo.getNom().replace('%20',' ').replace('%28',' ').replace('%29',' ').replace(' ','').replace('%C3',' ').replace('%A9',' ')+"%d"%(i)+".html";
            self.photoHtml(album,photo,lienhtml,titre,i,nbphoto,bool)
            nb = 18 + len(album.getNom())
            lien = lien[nb:len(lien)].replace('%','%25')
            i = i+1
            width = img.GetWidth()
            height = img.GetHeight()     
            if(height < width ):
                indexAlbums.write("<td align='center' height='140' width='140' style='background-color:#798073' ><a href='grandes/"+lienhtml+"'><img src='"+lien+"' border='0' width='135px' /></a></td>")
                libel = libel + "<td align='center'> <a  href='grandes/"+lienhtml+"'>"+nom +"</a></td>"
            else :
                indexAlbums.write("<td align='center'height='140' width='140' style='background-color:#798073' ><a  href='grandes/"+lienhtml+"'><img src='"+lien+"' border='0' height='130px' /></a></td>")
                libel = libel + "<td align='center'> <a  href='grandes/"+lienhtml+"'>"+nom +"</a></td>"
            if(i%7 == 0):
                libel = libel + "</tr>"
                indexAlbums.write(libel)
                libel ="<tr>"
        if(i%7 != 0):
            libel = libel + "</tr>"
            indexAlbums.write(libel)
            libel ="<tr>"
            #indexAlbums.write("<tr><td style='background-color:#798073'><a href='"+photo[17:len(photo)]+"'>"+photo[17:len(photo)]+" </a></td></tr>")
        indexAlbums.write("</TABLE></BODY></HTML>")
        indexAlbums.close()
        
    def photoHtml(self,album,photo,lienPhoto,titre,id,nbphoto,bool):
        indexAlbums = open('./data/mesAlbums/'+album.getNom()+'/grandes/'+lienPhoto,'w')
        indexAlbums.write("<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//FR' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>")
        indexAlbums.write("<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='fr' lang='fr'><HEAD><meta http-equiv='Content-Type' content='text/html; charset=utf-8' />")
        indexAlbums.write("<TITLE>"+titre+"HTML</TITLE></HEAD>")
        indexAlbums.write("<BODY style='background-color:#798073'>")
        indice = "  %d / %d  " % (id+1,nbphoto)
        indexAlbums.write("<TABLE align='center' style='background-color:#798073'>")
        
        ''' recuperation du lien de la photo precedente '''
        if(id>0):
            photoa = album.getListeMiniatures()[id-1]
            lienhtml = photoa.getNom().replace('%20',' ').replace('%28',' ').replace('%29',' ').replace(' ','').replace('%C3',' ').replace('%A9',' ')+"%d"%(id-1)+".html";
            indexAlbums.write("<tr><td width='50px'><a href='"+lienhtml+"'>Precedente</a></td><td width='80px'></td>")
        else:
            indexAlbums.write("<tr><td width='50px'></td><td width='80px'></td>")
        
        if(bool):
            indexAlbums.write("<td align='center' ><H2 align='center'><a href='../../index.html'>"+titre+"</a> > </H2></td>") 
 
        indexAlbums.write("<td align='center'><H3 align='center'> Album : <a href='../index.html'>"+album.getNom()+"</a> > </H3></td>")    
        indexAlbums.write("<td align='center'><H4 align='center'> Photo : "+photo.getNom().replace('%20',' ').replace('%28',' ').replace('%29',' ').replace('%C3',' ').replace('%A9',' ')+" : </H4>") 
        indexAlbums.write("<td align='center' style='color:#FFF' >"+indice+"<td>")
        
        if(id<nbphoto-1):
            photob = album.getListeMiniatures()[id+1]
            lienhtml = photob.getNom().replace('%20',' ').replace('%28',' ').replace('%29',' ').replace(' ','').replace('%C3',' ').replace('%A9',' ')+"%d"%(id+1)+".html";              
            indexAlbums.write("<td width='80px'></td><td width='50px' align='left'><a href='"+lienhtml+"'>       Suivante</a></td></tr>")
        else:
            indexAlbums.write("<td width='80px'></td><td width='50px'></td></tr>")
        
        indexAlbums.write("</table><TABLE align='center' border='0' style='background-color:#798073'>")
        indexAlbums.write("<tr><td></td></tr><tr>")
        ''' cc '''
        lien = photo.getChemin()
        img = wxImage(lien)
        nom = photo.getTitre().replace('%20',' ').replace('%28',' ').replace('%29',' ')
        if(len(nom)<5):
            nom = photo.getNom().replace('%20',' ').replace('%28',' ').replace('%29',' ');
        ''' enlever minis/ '''
        nb = 24 + len(album.getNom())
        lien = lien[nb:len(lien)].replace('%','%25')
        width = img.GetWidth()
        height = img.GetHeight()     
        
        indexAlbums.write("<tr>")

        ''' on affiche l'image entre precedente et suivant en fonction de sa taille'''
        if(height < width ):
            indexAlbums.write("<td align='center' width='600px' style='background-color:#798073' ><img src='"+lien+"' border='0' width='800px' /></td>")
        else :
            indexAlbums.write("<td align='center' width='600px' style='background-color:#798073' ><img src='"+lien+"' border='0' height='500px' /></td>")
        ''' fin d'affichage de 'limage '''
        

        indexAlbums.write("</tr><tr><td style='background-color:#FFF'align='center'>"+nom +"</td></tr>")

        indexAlbums.write("</TABLE></BODY></HTML>")
        indexAlbums.close()
        
        
    def cprep(self,src,dest):
        #src = "../data/mesAlbums/"
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
        fs=open(src,"rb")
        fd=open(dest,"wb")
    
        for line in fs:
            fd.write(line)
    
        fs.close()
        fd.close()
    

