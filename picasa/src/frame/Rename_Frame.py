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

class Rename_Frame(wxFrame):
    '''
    classdocs  Rename_Frame(parent, ID, title,name,sizeX,sizeY)
    '''

    name =""
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

        font = wxSystemSettings_GetFont(wxSYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wxBoxSizer(wxVERTICAL)

        hbox1 = wxBoxSizer(wxHORIZONTAL)
        st1 = wxStaticText(panel, -1, "Ancien nom de l'album")
        st1.SetFont(font)
        hbox1.Add(st1, 0, wxRIGHT, 8)
        self.tc = wxTextCtrl(panel, -1)
        self.tc.SetValue(self.name)
        hbox1.Add(self.tc, 1)
        vbox.Add(hbox1, 0, wxEXPAND | wxLEFT | wxRIGHT | wxTOP, 10)

        vbox.Add((-1, 10))

        hbox2 = wxBoxSizer(wxHORIZONTAL)
        st2 = wxStaticText(panel, -1, "Nouveau nom de l'album")
        st2.SetFont(font)
        hbox2.Add(st2, 0, wxRIGHT, 8)
        self.tc2 = wxTextCtrl(panel, -1)
        hbox2.Add(self.tc2, 1)
        vbox.Add(hbox2, 0, wxEXPAND | wxLEFT | wxRIGHT | wxTOP, 10)

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
        
        if (nameA != nameN) & (len(nameN) > 3):
            try :
                self.parent.MyAlbums.renommerAlbum(self.name,nameN)
            except IOError:
                self.afficheErrorMsg("I/O error({0}): {1}")
            except ValueError:
                self.afficheErrorMsg("L'album existe deja !!! \n ( soit en temps que nom soit l'url est deja utilise")
            except:
                self.afficheErrorMsg("Une erreur est survenu merci de verifier l'url !!! ")
            self.parent.afficheAlbums()
            self.Close(true)  
               
        else:
            self.afficheMsgErreur()
    
    
    def OnAnnule(self,event):
        self.Close(true)
        

    def afficheErrorMsg(self,msg):    
            dlg = wxMessageDialog(self,msg,
                                  "Message d'erreur", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
    
        
    def afficheMsgErreur(self):
            dlg = wxMessageDialog(self," Le nom de l'albums est invalide :\n\n"
                                  "- le nom de l'album doit comporter au mois 4 caracteres  \n"
                                  "- il est inutile de renommer un album avec le meme nom \n\n",
                                  "Message d'erreur", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
    
