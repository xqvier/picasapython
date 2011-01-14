# -*- coding: iso-8859-15 -*-
'''
Created on 9 janv. 2011

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

class Confirme_Supr_Frame(wxFrame):
    '''
    classdocs   
    '''
    name = ""

    def __init__(self, parent, ID, title,name,sizeX,sizeY):
        '''
        Constructor
        '''
        wxFrame.__init__(self, parent, ID, title,
                             wxDefaultPosition, wxSize(sizeX,sizeY))
        self.parent = parent
        self.SetBackgroundColour("white")
        self.name = name
        ''' definition d'un panel pour mettre en place les champs et boutton '''
        panel = wxPanel(self, -1)


        vbox = wxBoxSizer(wxVERTICAL)

        hbox1 = wxBoxSizer(wxHORIZONTAL)
        st1 = wxStaticText(panel, -1, "Vous allez supprimer l'album suivant:")
        hbox1.Add(st1, 0, wxRIGHT, 8)
        vbox.Add(hbox1, 0, wxEXPAND | wxLEFT | wxRIGHT | wxTOP, 10)

        vbox.Add((-1, 10))

        hbox2 = wxBoxSizer(wxHORIZONTAL)
        st2 = wxStaticText(panel, -1,self.name)
        hbox2.Add(st2, 0)
        vbox.Add(hbox2, 0, wxCENTER | wxTOP, 10)

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

            try :
                self.parent.MyAlbums.retraitAlbum(self.name)
            except IOError:
                self.afficheErrorMsg("I/O error({0}): {1}")
            except ValueError:
                self.afficheErrorMsg("L'album n'existe pas!")
            except:
                self.afficheErrorMsg("Une erreur est survenu impossible de supprimer l'album!")
            self.parent.afficheAlbums()
            self.Close(true)  
               

    
    
    def OnAnnule(self,event):
        self.Close(true)
        

    def afficheErrorMsg(self,msg):    
            dlg = wxMessageDialog(self,msg,
                                  "Message d'erreur", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
    
        
        
