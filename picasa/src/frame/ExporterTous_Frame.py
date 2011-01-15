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
from Export import Export


from wxPython.wx import *
from wx._core import KeyEvent

''' definition des constantes des bouton'''
Id_VAL = 10
Id_ANN = 11

class ExporterTous_Frame(wxFrame):
    '''
    classdocs  Rename_Frame(parent, ID, title,name,sizeX,sizeY)
    '''
    albums = ""
    export = ""
    name =""
    def __init__(self, parent, ID, title,albums,sizeX,sizeY):
        '''
        Constructor
        '''
        wxFrame.__init__(self, parent, ID, title,
                             wxDefaultPosition, wxSize(sizeX,sizeY))
        self.parent = parent
        self.SetBackgroundColour("white")
        self.name = "Picasa Albums"
        self.albums = albums
        self.export = Export()
        ''' definition d'un panel pour mettre en place les champs et boutton '''
        panel = wxPanel(self, -1)

        font = wxSystemSettings_GetFont(wxSYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wxBoxSizer(wxVERTICAL)

        hbox1 = wxBoxSizer(wxHORIZONTAL)
        st1 = wxStaticText(panel, -1, "Nom du dossier:")
        st1.SetFont(font)
        hbox1.Add(st1, 0, wxRIGHT, 8)
        self.tc = wxTextCtrl(panel, -1)
        self.tc.SetValue(self.name)
        hbox1.Add(self.tc, 1)
        vbox.Add(hbox1, 0, wxEXPAND | wxLEFT | wxRIGHT | wxTOP, 10)

        vbox.Add((-1, 10))

        hbox2 = wxBoxSizer(wxHORIZONTAL)
        st2 = wxStaticText(panel, -1, "Titre des fenetre html")
        st2.SetFont(font)
        hbox2.Add(st2, 0, wxRIGHT, 8)
        self.tc2 = wxTextCtrl(panel, -1)
        self.tc2.SetValue(self.name)
        hbox2.Add(self.tc2, 1)
        vbox.Add(hbox2, 0, wxEXPAND | wxLEFT | wxRIGHT | wxTOP, 10)

        vbox.Add((-1, 10))

        hbox4 = wxBoxSizer(wxHORIZONTAL)
        st4 = wxStaticText(panel, -1, "Url d'export :")
        st4.SetFont(font)
        hbox4.Add(st4, 0)
        vbox.Add(hbox4, 0, wxLEFT | wxTOP, 10)
        
        vbox.Add((-1, 10))
        
        hbox3 = wxBoxSizer(wxHORIZONTAL)
        self.tc3 = wxTextCtrl(panel, -1, style=wxTE_MULTILINE)
        hbox3.Add(self.tc3, 1, wxEXPAND)
        vbox.Add(hbox3, 1, wxLEFT | wxRIGHT | wxEXPAND, 10)
                 
        vbox.Add((-1, 25))

        hbox5 = wxBoxSizer(wxHORIZONTAL)
        btn1 = wxButton(panel,Id_VAL, 'Valider', size=(70, 30))
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
        nameA = self.tc.GetValue()
        nameN = self.tc2.GetValue()
        src = './data/mesAlbums/'
        dest = self.tc3.GetValue()
        if dest.endswith('/'):
            dest = dest + nameA
        else:
            dest = dest +'/'+ nameN
        if (len(nameN) > 3):
            try :
                self.export.indexAlbums(self.albums,nameN)  
                self.export.cprep(src,dest)
            except IOError:
                self.afficheMsgErreur()
            except ValueError, e:
                self.afficheMsgErreur()
            except:
                self.afficheMsgErreur()
        self.parent.afficheAlbums()
        self.Close(true)  
               
    
    
    def OnAnnule(self,event):
        self.Close(true)
        

    def afficheErrorMsg(self,msg):    
            dlg = wxMessageDialog(self,msg,
                                  "Message d'erreur", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
    
        
    def afficheMsgErreur(self):
            dlg = wxMessageDialog(self,"L'url d'export est invalide :\n\n"
                                  "- ex: C:\Users\Silou\Desktop\Test_Copy_python \n"
                                  "- Verifier les droits du dossier.\n\n",
                                  "Message d'erreur", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
    
