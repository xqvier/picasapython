# -*- coding: iso-8859-15 -*-
'''
Created on 8 janv. 2011

@author: Silou
'''
import sys

sys.path.append('./class')
from Albums import Albums
from Album import Album
from Photo import Photo

from wxPython.wx import *
from wx._core import KeyEvent

''' definition des constantes des bouton'''
Id_VAL = 10
Id_ANN = 11

class MyAjoutFrame(wxFrame):
    '''
    classdocs
    '''


    def __init__(self, parent, ID, title,sizeX,sizeY):
        '''
        Constructor
        '''
        wxFrame.__init__(self, parent, ID, title,
                             wxDefaultPosition, wxSize(sizeX,sizeY))
        self.parent = parent
        self.SetBackgroundColour("white")

        ''' definition d'un panel pour mettre en place les champs et boutton '''
        panel = wxPanel(self, -1)

        font = wxSystemSettings_GetFont(wxSYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wxBoxSizer(wxVERTICAL)

        hbox1 = wxBoxSizer(wxHORIZONTAL)
        st1 = wxStaticText(panel, -1, "Nom de l'album :")
        st1.SetFont(font)
        hbox1.Add(st1, 0, wxRIGHT, 8)
        self.tc = wxTextCtrl(panel, -1)
        hbox1.Add(self.tc, 1)
        vbox.Add(hbox1, 0, wxEXPAND | wxLEFT | wxRIGHT | wxTOP, 10)

        vbox.Add((-1, 10))

        hbox2 = wxBoxSizer(wxHORIZONTAL)
        st2 = wxStaticText(panel, -1, "Url de l'album :")
        st2.SetFont(font)
        hbox2.Add(st2, 0)
        vbox.Add(hbox2, 0, wxLEFT | wxTOP, 10)

        vbox.Add((-1, 10))

        hbox3 = wxBoxSizer(wxHORIZONTAL)
        self.tc2 = wxTextCtrl(panel, -1, style=wxTE_MULTILINE)
        hbox3.Add(self.tc2, 1, wxEXPAND)
        vbox.Add(hbox3, 1, wxLEFT | wxRIGHT | wxEXPAND, 10)


        vbox.Add((-1, 25))

        hbox5 = wxBoxSizer(wxHORIZONTAL)
        btn1 = wxButton(panel,Id_VAL, 'Ajouter', size=(70, 30))
        btn2 = wxButton(panel,Id_ANN, 'Annuler', size=(70, 30))
        hbox5.Add(btn2, 0)
        hbox5.Add(btn1, 0, wxLEFT | wxBOTTOM , 5)
        vbox.Add(hbox5, 0, wxALIGN_RIGHT | wxRIGHT, 10)
        
        EVT_BUTTON(self,Id_VAL,self.OnValide)
        EVT_BUTTON(self,Id_ANN,self.OnAnnule)
        
        panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)
        
    
    def OnValide(self,event):
        name = self.tc.GetValue()
        url = self.tc2.GetValue()
        
        if (len(name) > 3 & url.startswith("http://picasaweb.google.com/") ):
            try :
                self.patienterMsg()
                self.parent.MyAlbums.ajouterAlbum(name,url) 
            except IOError:
                self.afficheErrorMsg("I/O error({0}): {1}")
            except ValueError:
                self.afficheErrorMsg("L'album existe deja! \n (soit en temps que nom, soit l'url est deja utilise")
            except:
                self.afficheErrorMsg("Une erreur est survenu merci de verifier l'url!")
            self.parent.afficheAlbums()
	    self.Close(True)  
               
        else:
            self.afficheMsgErreur()
    
    
    def OnAnnule(self,event):
        self.Close(True)
        
    def patienterMsg(self):    
            dlg = wxMessageDialog(self,"Merci de patienter durant le chargements des images. \n\n Cette fenetre se fermera a la fin du chargement",
                                  "Chargement des images...", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
    def afficheErrorMsg(self,msg):    
            dlg = wxMessageDialog(self,msg,
                                  "Message d'erreur...", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
    
        
    def afficheMsgErreur(self):
            dlg = wxMessageDialog(self,"L'url ou le nom de l'album est invalide :\n\n"
                                  "- Le nom de l'album doit comporter au moins 4 caractères.\n"
                                  "- L'url de l'album doit contenir http://picasaweb.google.com/.\n"
                                  "- Verifiez votre connexion a internet \n\n",
                                  "Message d'erreur", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
    
