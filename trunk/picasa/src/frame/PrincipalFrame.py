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
from AjoutFrame import MyAjoutFrame
from Confirme_Supr_Frame import Confirme_Supr_Frame
from Rename_Frame import Rename_Frame

''' definition des constantes des bouton du menu '''
ID_AIDE = 100
ID_ABOUT = 101
ID_EXIT  = 102
ID_AJOUT = 103
ID_SUP = 104
ID_REN = 105
ID_SYNC = 106
ID_REC = 107
ID_TLA = 108
ID_TLA2 = 109
INDEX = 10003
IND_P = 1001
''' taille de la fenetre d'ajout d'album '''
ajout_size_x = 500
ajout_size_y = 300
''' taille des miniature '''
photoX = 144
photoY = 144
fen_size_x = 1065
fen_size_y = 700
    
class MyFrame(wxFrame):
    '''
    Cette class est la fenetre principale elle permet de gerer graphiquement des albums picassa
    '''
    PR_NAME = ""
    MyAlbums = NULL
    AlbumEnCours = -1
    PhotoEnCours = -1
    ''' Constructeur de la class '''
    def __init__(self, parent, ID, title,sizeX,sizeY):
            wxFrame.__init__(self, parent, ID, title,
                             wxDefaultPosition, wxSize(sizeX,sizeY))
            ''' recuperation du titre de l'application'''
            self.PR_NAME = title
            ''' recuperation de la fenetre parent '''
            self.parent = parent
            ''' instanciation de la classe album afin de pouvoir ajouter,creer,acceder les albums '''
            self.MyAlbums = Albums()
            ''' recuperation des evenement du clavier '''
            EVT_KEY_DOWN(self,self.press_key)
            ''' initialisation du menu '''
            self.initializeMenu()
            ''' initialisation du contenu '''
            self.initializeContenu()
            ''' modification de la taille de la fenetre '''
            EVT_SIZE(self,self.resize)

            
            
    ''' ----------------------------------------------------------------------------------------------------
        ***************************** Initialisation du contenu ********************************************
        ----------------------------------------------------------------------------------------------------
    '''    
    def initializeContenu(self):
            self.panel = wxPanel(self, -1,(0,0),wxSize(2000,2000))
            self.panel.SetBackgroundColour('#4f5049')
            vbox = wxBoxSizer(wxVERTICAL)
            midPan = wxPanel(self.panel, -1,)
            midPan.SetBackgroundColour('white')
            vbox.Add(midPan, 1, wxALL | wxALL, 20)
            self.panel.SetSizer(vbox)
            self.Centre()
            self.Show(True)  
            self.panel.DestroyChildren()
            self.afficheAlbums()
            
    def resize(self,event):
        # retailler la fennetre 
        print ""
        
        
    def afficheAlbums(self):
            self.PhotoEnCours = -1
            self.panel.DestroyChildren()
            vbox = wxBoxSizer(wxVERTICAL)
            self.AlbumEnCours = -1;
            self.SetStatusText("Aucun albums selectionne !!!")
            navig_panel = wxPanel(self.panel, 10,(0,10),wxSize(2000,40))
            navig_panel.SetBackgroundColour('#4f5049')
            midPan = wxPanel(self.panel, 10,(35,70),wxSize(fen_size_x,fen_size_y))
            midPan.SetBackgroundColour('white')
            
            index = INDEX
            posX = 10
            posY = 10
            size = wxSize(photoX,photoY)
            wxButton(navig_panel,ID_TLA2,"Tous les albums",(posX/2,posY),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
            EVT_BUTTON(self,ID_TLA2,self.afficheAlbumsE)
            for i in self.MyAlbums.getAlbums():
                nom = i.getNom()
                a = i.getListeMiniatures()
                img = a[0].getChemin()
                imge = wxImage(img,wxBITMAP_TYPE_ANY, -1).ConvertToBitmap()
                wxBitmapButton(midPan,index, imge,(posX,posY),size, wxNO_BORDER, wxDefaultValidator,nom)
                st = wxStaticText(midPan,-1,nom,(posX+50,posY+150),wxSize(144,20))
                st.Show(True)  
                EVT_BUTTON(self,index,self.OnAfficheAlbum)
                index += 1
                posX += 150
                if(index%7 == 0):
                    posY += 170
                    posX = 10
            vbox.Add(navig_panel,0,wxALL | wxALL,20)
            vbox.Add(midPan, 1, wxALL | wxALL, 20)
            self.panel.SetSizer(vbox)
            self.Centre()
            self.Show(True)  

    def OnAfficheAlbum(self,event):
        self.PhotoEnCours = -1
        self.panel.DestroyChildren()
        vbox = wxBoxSizer(wxVERTICAL)
        navig_panel = wxPanel(self.panel, 10,(0,10),wxSize(2000,40))
        navig_panel.SetBackgroundColour('#4f5049')
        midPan = wxPanel(self.panel, 10,(35,70),wxSize(fen_size_x,fen_size_y))
        midPan.SetBackgroundColour('white')
        index = IND_P
        posX = 10
        posY = 10
        size = wxSize(photoX,photoY)
        albums = self.MyAlbums.getAlbums()
        self.AlbumEnCours = event.GetId()-INDEX
        album = albums[event.GetId()-INDEX]
        self.SetStatusText("En cours : " + album.getNom())
        wxButton(navig_panel,ID_TLA2,"Tous les albums >>",(posX/2,posY),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
        EVT_BUTTON(self,ID_TLA2,self.afficheAlbumsE)
        wxButton(navig_panel,event.GetId(),album.getNom()+" >",(posX/2 +110,posY),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
        EVT_BUTTON(self,event.GetId(),self.OnAfficheAlbum)
        st = wxStaticText(navig_panel,-1,album.getUrl(),(230,20),wxSize(600, 30), wxNO_BORDER)
        st.SetForegroundColour("white")
        for a in album.getListeMiniatures():
            img = a.getChemin()
            imge = wxImage(img,wxBITMAP_TYPE_ANY, -1).ConvertToBitmap()
            id = event.GetId()*100000+index
            wxBitmapButton(midPan,id, imge,(posX,posY),size, wxNO_BORDER, wxDefaultValidator)
            EVT_BUTTON(self,id,self.OnAffichePhoto)
            index += 1
            posX += 150
            if(index%7 == 0):
                posY += 150
                posX = 10
        wxScrollBar(midPan,5,(fen_size_x-15,0),wxSize(15,fen_size_y),wxNO_BORDER,wxDefaultValidator,"scroll")
        vbox.Add(navig_panel,0,wxALL | wxALL,20)
        vbox.Add(midPan, 1, wxALL | wxALL, 20)
        self.panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)  
        
    def OnAffichePhoto(self,event):
        ''' albums id '''
        if(event.GetId()>99999):
            i =  event.GetId()/100000
            self.AlbumEnCours = i-INDEX
            ''' photo id '''
            p =  event.GetId() - i*100000
            vbox = wxBoxSizer(wxVERTICAL)
        else :
            i = self.AlbumEnCours + INDEX
            p = event.GetId()
        #print "id de l'album :",i
        #print "id de la photo :",p
        self.PhotoEnCours = p
        albums = self.MyAlbums.getAlbums()
        album = albums[i-INDEX]
        photos = album.getListeGrandes()
        photo = photos[p-IND_P]
        ch = photo.getChemin()
        img = wxImage(ch,wxBITMAP_TYPE_ANY, -1).ConvertToBitmap()
        self.panel.DestroyChildren()
        ''' bouton de navigation '''
        navig_panel = wxPanel(self.panel, 10,(0,10),wxSize(2000,40))
        navig_panel.SetBackgroundColour('#4f5049')
        wxButton(navig_panel,ID_TLA2,"Tous les albums >>",(10,10),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
        EVT_BUTTON(self,event.GetId(),self.afficheAlbumsE)
        wxButton(navig_panel,i,album.getNom()+" >",(120,10),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
        EVT_BUTTON(self,i,self.OnAfficheAlbum)
        st = wxStaticText(navig_panel,p,photo.getNom(),(230,20),wxSize(300, 30), wxNO_BORDER)
        st.SetForegroundColour("white")
        text =  "%d / %d" %((p-IND_P+1),len(album.getListeGrandes()))
        st = wxStaticText(navig_panel,-1,text,(740,20),wxSize(100, 30), wxNO_BORDER)
        st.SetForegroundColour("white")
        if(len(album.getListeGrandes()) > (p-IND_P+1)):
            wxButton(navig_panel,(p+1),"Suivante >",(850,10),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
            EVT_BUTTON(self,(p+1),self.OnAffichePhoto)
        if(p-IND_P >= 1):
            wxButton(navig_panel,(p-1),"< Precedente",(550,10),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
            EVT_BUTTON(self,(p-1),self.OnAffichePhoto)
        ''' mise a lechelle de l'image '''
        width =   img.GetWidth()
        height =  img.GetHeight()
        width1 = width
        width2 = width1
        height1 = height
        height2 = height1 
        if(width > fen_size_x):
            width1 = fen_size_x
            height1 = (fen_size_x*height)/width
            height2 = height1
            width2 = width1 
        if(height1 > fen_size_y):
            height2 = fen_size_y
            width2 = (fen_size_y*width1)/height1
        
        img.SetSize(wxSize(width2,height2))
        
        ''' calcul de la position central de l'image '''
        PosX = ((fen_size_x+75)/2)-(width2/2)
        PosY = 70
        wxStaticBitmap(self.panel, 10,img,(PosX,PosY),wxSize(width2,height2))
        self.Centre()
        self.Show(True)  
        
    def OnClose(self, event):
        self.Close()

    
    
        
    ''' Recuper les evenement du clavier  
            Affiche l'aide lors de l'appuis de F1
            Change la selection des albums ou photo grace au fleche
            WXK_F1    WXK_LEFT    WXK_UP    WXK_RIGHT    WXK_DOWN
    '''    
    def press_key(self,event):
            key = event.GetKeyCode()
            print key
            if(key == WXK_LEFT):
                print "fleche gauche"
                if(self.PhotoEnCours != -1 & self.AlbumEnCours!=-1):
                    albums = self.MyAlbums.getAlbums()
                    album = albums[self.AlbumEnCours-INDEX]

                    if(len(album.getListeGrandes()) > (self.PhotoEnCours-IND_P+1)):
                        Event = EVT_BUTTON(self,(self.PhotoEnCours+1),self.OnAffichePhoto)
                        self.OnAffichePhoto(Event)

            elif(key == WXK_RIGHT):
                print "fleche droite"
                if(self.PhotoEnCours != -1 & self.AlbumEnCours!=-1):
                    if(self.PhotoEnCours-IND_P >= 1):
                        Event = EVT_BUTTON(self,(self.PhotoEnCours-1),self.OnAffichePhoto)
                        self.OnAffichePhoto(Event)
            elif(key == WXK_UP):
                self.OnAide(event)                      
            event.Skip()
            
            
    ''' ----------------------------------------------------------------------------------------------------
        *****************************  FIN Initialisation du contenu ********************************************
        ----------------------------------------------------------------------------------------------------
    '''         









    ''' ----------------------------------------------------------------------------------------------------
        ******************** Initialisation de la barre de menu ********************************************
        ----------------------------------------------------------------------------------------------------
    '''
    def initializeMenu(self):
            ''' modification de la couleur du fond en blanc pour plus de convivialite '''
            self.SetBackgroundColour("white")
            
            ''' La barre de status va nous permettre de definir les albums en cours '''
            self.CreateStatusBar()
            self.SetStatusText("Aucun albums selectionne !!!")
    
            ''' instanciation de la barre de menu '''
            menuBar = wxMenuBar()
    
            ''' defenition du menu fichier '''
            menu = wxMenu()
            menu.Append(ID_TLA, "&Tous les albums", "Affiche tous les albums")
            menu.AppendSeparator()
            menu.Append(ID_EXIT, "&Quitter", "Termine ")
            menuBar.Append(menu, "&Fichier");
            EVT_MENU(self, ID_EXIT,self.TimeToQuit)
            EVT_MENU(self, ID_TLA,self.afficheAlbumsE)
            
            ''' defenition du menu Edition '''
            menuEdit = wxMenu()
            menuEdit.Append(ID_AJOUT, "Ajouter un album",
                        "Permet d'ajouter un albums picassa par son URL.")
            menuEdit.AppendSeparator()
            menuEdit.Append(ID_SYNC, "Actualiser l'album",
                        "Permet de rafraichier un albums picassa par son URL.")
            menuEdit.Append(ID_REN, "Renommer l'album",
                        "Permet de renommer un albums picassa.")
            menuEdit.Append(ID_SUP, "Supprimer l'album",
                        "Permet de supprimer un albums picassa.")
            menuEdit.AppendSeparator()
            menuEdit.Append(ID_REC, "Recherche un album",
                        "Permet de rechercher un albums picassa.")
            menuBar.Append(menuEdit, "&Edition");
            EVT_MENU(self, ID_AJOUT, self.AjoutAlbum)
            EVT_MENU(self, ID_SYNC, self.SyncAlbum)
            EVT_MENU(self, ID_REN, self.RenaAlbum)
            EVT_MENU(self, ID_SUP, self.SuprAlbum)
            EVT_MENU(self, ID_REC, self.RechAlbum)
            
            ''' definition du menu aide '''
            menuAide = wxMenu()
            menuAide.Append(ID_AIDE, "&Aide                                          F1",
                        "Affiche une fenetre d'aide du logiciel")
            menuAide.AppendSeparator()
            menuAide.Append(ID_ABOUT, "&A propos de "+self.PR_NAME,
                        "Plus d'information sur le programme")
            menuBar.Append(menuAide, "&?");
            EVT_MENU(self, ID_ABOUT, self.OnAbout)
            EVT_MENU(self, ID_AIDE, self.OnAide)
            
            ''' ajout de la barre de menu a la fenetre '''
            self.SetMenuBar(menuBar)   
                     
    ''' fonction apppele par evenement pour afficher tous les albums '''
    def afficheAlbumsE(self,event):
        self.afficheAlbums()
        
    ''' affiche une message de dialogue definissant l'application '''
    def OnAbout(self, event):
            dlg = wxMessageDialog(self,self.PR_NAME+" :\n\n"
                                      "Ce programme permet de telecharger des albums picassa,\n"
                                      "de les sauvegarder,visualiser et supprimer.\n\n"
                                      "By : \n\n   Maxime Rodrigues \n    Xavier Mourgues \n    Sylvain Picalre",
                                      "A Propos", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
    
    ''' permet de fermer la fenetre '''
    def TimeToQuit(self, event):
            self.Close(true)
        

    ''' affiche une message de dialogue definissant l'application '''
    def OnAide(self, event):
            dlg = wxMessageDialog(self,self.PR_NAME+" fichier d'aide :\n\n"
                                      "Ce programme permet de telecharger des albums picassa,\n"
                                      "de les sauvegarder,visualiser et supprimer.\n\n"
                                      "By : \n\n   Maxime Rodrigues \n    Xavier Mourgues \n    Sylvain Picalre",
                                      "Aide    F1", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    ''' permet d'ajouter un album :
            ouvre une fenetre permet de saisir les differents parametre de l'albums
    '''
    def AjoutAlbum(self,event):
            frame = MyAjoutFrame(self,-2,"Ajout d'un albums",ajout_size_x,ajout_size_y )
            frame.Show(true)
            #self.SetTopWindow(frame)
            
    ''' permet de rechercher un albums non visible sur le champs et de le selectionne '''
    def RechAlbum(self,event):
       self.afficheAlbums()

    ''' permet de rafraichir l'albums en cours '''
    def SyncAlbum(self,event):
            if self.AlbumEnCours == -1:
                self.MsgAucunSelect()
            else:
                #print "Actulisation de l'album", self.AlbumEnCours
                self.AlbumEnCours
                albums = self.MyAlbums.getAlbums()
                album = albums[self.AlbumEnCours]
                self.MyAlbums.sync(album.getNom())
    
    ''' permet de renommer un albums '''
    def RenaAlbum(self,event):
            if self.AlbumEnCours == -1:
                self.MsgAucunSelect()
            else:
                self.AlbumEnCours
                albums = self.MyAlbums.getAlbums()
                album = albums[self.AlbumEnCours]
                #print "Rename de l'album" , album.getNom()
                frame = Rename_Frame(self, -1,"Renommer un album",album.getNom(),350,180)
                frame.Show(True)
        
    ''' permet de supprimer un albums '''
    def SuprAlbum(self,event):
            if self.AlbumEnCours == -1:
                self.MsgAucunSelect()
            else:
                albums = self.MyAlbums.getAlbums()
                album = albums[self.AlbumEnCours]
                #print "Suppression de l'album",album.getNom()
                frame = Confirme_Supr_Frame(self, -1,"Confirmation de suppression de l'album",album.getNom(),350,180)
                frame.Show(True)
              
    ''' affiche une erreur comme quoi il faut selectionner un albums '''
    def MsgAucunSelect(self):
            dlg = wxMessageDialog(self,self.PR_NAME+"Aucun albums n'est selectionner !!!\n\n"
                                          "Selectionner un albums,\n"
                                          "Si aucun alnums exist ajouter en un Edition -> Ajouter.\n\n",
                                          "Message d'erreur", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
    
    
    ''' ------------------------------------------------------------------------------------------------
    ******************** FIN  Initialisation de la barre de menu ***************************************
    ----------------------------------------------------------------------------------------------------
    '''
