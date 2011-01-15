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
from AjoutFrame import MyAjoutFrame
from Confirme_Supr_Frame import Confirme_Supr_Frame
from Rename_Frame import Rename_Frame

''' definition des constantes des bouton du menu '''
ID_AIDE = 0
ID_ABOUT = 1
ID_EXIT  = 2
ID_AJOUT = 3
ID_SUP = 4
ID_REN = 5
ID_SYNC = 6
ID_REC = 7
ID_TLA = 8
ID_TLA2 = 9
INDEX = 14
IND_P = 105
''' taille de la fenetre d'ajout d'album '''
ajout_size_x = 500
ajout_size_y = 200
''' taille des miniature '''
photoX = 144
photoY = 144
cadrephotoX = 144
cadrephotoY = 170
fen_size_x = 1065
fen_size_y = 620
    
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
	    self.cacheMenu(True)
            self.PhotoEnCours = -1
            self.panel.DestroyChildren()
            vbox = wxBoxSizer(wxVERTICAL)
            self.AlbumEnCours = -1;
            self.SetStatusText("Aucun album selectionne!")
            navig_panel = wxPanel(self.panel, 10,(0,10),wxSize(2000,40))
            navig_panel.SetBackgroundColour('#4f5049')
            midPan = wxScrolledWindow(self.panel, 10,(35,70),wxSize(fen_size_x,fen_size_y))
            midPan.SetBackgroundColour('white')
	    midPan.SetScrollbars(0, 1, 0, (len(self.MyAlbums.getAlbums()) /6) * cadrephotoY)
            index = INDEX
            posX = 10
            posY = 10
            size = wxSize(photoX,photoY)
            wxButton(navig_panel,ID_TLA2,"Mes albums",(posX/2,posY),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
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
	self.cacheMenu(False)
        self.PhotoEnCours = -1
        self.panel.DestroyChildren()
        vbox = wxBoxSizer(wxVERTICAL)
        navig_panel = wxPanel(self.panel, 10,(0,10),wxSize(2000,40))
        navig_panel.SetBackgroundColour('#4f5049')
	midPan = wxScrolledWindow(self.panel, 10,(35,70),wxSize(fen_size_x,fen_size_y))
        midPan.SetBackgroundColour('white')
        index = IND_P
        posX = 10
        posY = 10
        size = wxSize(photoX,photoY)
        albums = self.MyAlbums.getAlbums()
        self.AlbumEnCours = event.GetId()-INDEX
        album = albums[event.GetId()-INDEX]
	midPan.SetScrollbars(0, 1, 0, (len(album.getListeMiniatures()) /6) * cadrephotoY)
        self.SetStatusText("En cours : " + album.getNom())
        wxButton(navig_panel,ID_TLA2,"Mes albums",(posX/2,posY),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
        EVT_BUTTON(self,ID_TLA2,self.afficheAlbumsE)
        wxButton(navig_panel,event.GetId(),album.getNom(),(posX/2 +110,posY),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
        EVT_BUTTON(self,event.GetId(),self.OnAfficheAlbum)
        st = wxStaticText(navig_panel,-1,album.getUrl(),(230,20),wxSize(600, 30), wxNO_BORDER)
        st.SetForegroundColour("white")
        for a in album.getListeMiniatures():
            img = a.getChemin()
            imge = wxImage(img,wxBITMAP_TYPE_ANY, -1).ConvertToBitmap()
            id = event.GetId()+index*100
	    imgPan = wxPanel(midPan, id, (posX,posY),(cadrephotoX,cadrephotoY))
	    imgPan.SetBackgroundColour('white')
            wxBitmapButton(imgPan,id, imge,(0,0),size, wxNO_BORDER, wxDefaultValidator)
	    
	    titre = a.getTitre()
	    if len(titre)>17:
		titre = titre[0:17]+"..."
	    titre = wxStaticText(imgPan, wxID_ANY,titre, (posX,posY+photoY),wxSize(-1,-1))
            EVT_BUTTON(self,id,self.OnAffichePhoto)
            index += 1
            posX += 150
            if(index%7 == 0):
                posY += cadrephotoY
                posX = 10
	    titre.Center()
            pos = titre.GetPositionTuple()
	    titre.MoveXY(pos[0], photoY)
        vbox.Add(navig_panel,0,wxALL | wxALL,20)
        vbox.Add(midPan, 1, wxALL | wxALL, 20)
        self.panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)  
        
    def OnAffichePhoto(self,event):
	self.cacheMenu(False)
        ''' photo id '''
        if(event.GetId()>99):
            p =  event.GetId()/100         
            ''' albums id '''
            i =  event.GetId() - p*100
            self.AlbumEnCours = i-INDEX   
            vbox = wxBoxSizer(wxVERTICAL)
        else :
            i = self.AlbumEnCours + INDEX
            p = event.GetId() 
        self.PhotoEnCours = p
        albums = self.MyAlbums.getAlbums()
        album = albums[i-INDEX]
        photos = album.getListeGrandes()
        photo = photos[p-IND_P]
        ch = photo.getChemin()
        img = wxImage(ch,wxBITMAP_TYPE_ANY, -1)
        ''' mise a lechelle de l'image '''
        width =   img.GetWidth()
        height =  img.GetHeight()
	ratioX = float(width)/float(fen_size_x)
	ratioY = float(height)/float(fen_size_y)
	if ratioX>ratioY :
		ratio = float(ratioX)
	else : 
		ratio = float(ratioY)
	newwidth = width/ratio
	newheight = height/ratio
        img = img.Scale(newwidth, newheight)


	img = img.ConvertToBitmap()
        self.panel.DestroyChildren()
        ''' bouton de navigation '''
        navig_panel = wxPanel(self.panel, 10,(0,10),wxSize(2000,40))
        navig_panel.SetBackgroundColour('#4f5049')
        wxButton(navig_panel,ID_TLA2,"Mes albums",(10,10),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
        EVT_BUTTON(self,event.GetId(),self.afficheAlbumsE)
        wxButton(navig_panel,i,album.getNom(),(120,10),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
        EVT_BUTTON(self,i,self.OnAfficheAlbum)
        st = wxStaticText(navig_panel,p,photo.getNom(),(230,20),wxSize(300, 30), wxNO_BORDER)
        st.SetForegroundColour("white")
        text =  "%d / %d" %((p-IND_P+1),len(album.getListeGrandes()))
        st = wxStaticText(navig_panel,-1,text,(740,20),wxSize(100, 30), wxNO_BORDER)
        st.SetForegroundColour("white")
        if(len(album.getListeGrandes()) > (p-IND_P+1)):
            wxButton(navig_panel,(i+(p+1)*100),"Suivante >",(850,10),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
            EVT_BUTTON(self,(i+(p+1)*100),self.OnAffichePhoto)
        if(p-IND_P >= 1):
            wxButton(navig_panel,(i+(p-1)*100),"< Precedente",(550,10),wxSize(100, 30))#, wxNO_BORDER, wxDefaultValidator)
            EVT_BUTTON(self,(i+(p-1)*100),self.OnAffichePhoto)
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
    	titre = wxStaticText(self.panel, wxID_ANY,photo.getTitre(), (wxCENTER,fen_size_y + PosY),wxSize(-1,-1))
    	#titre.SetFont(wxFont(12,wxSWISS,wxDEFAULT,wxBOLD))
        font = wxSystemSettings_GetFont(wxSYS_SYSTEM_FONT)
        font.SetPointSize(12)
        titre.SetFont(font)
    	titre.Centre()
    	pos = titre.GetPositionTuple()
    	titre.MoveXY(pos[0], fen_size_y + PosY + 10)
    	titre.SetForegroundColour("white")
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
            self.SetStatusText("Aucun album selectionne!")
    
            ''' instanciation de la barre de menu '''
            menuBar = wxMenuBar()
    
            ''' defenition du menu fichier '''
            menu = wxMenu()
            menu.Append(ID_TLA, "Tous les albums", "Affiche tous les albums.")
            menu.AppendSeparator()
            menu.Append(ID_EXIT, "Quitter", "Termine ")
            menuBar.Append(menu, "Fichier");
            EVT_MENU(self, ID_EXIT,self.TimeToQuit)
            EVT_MENU(self, ID_TLA,self.afficheAlbumsE)
            
            ''' defenition du menu Edition '''
            self.menuEdit = wxMenu()
            self.menuEdit.Append(ID_AJOUT, "Ajouter un album...",
                        "Permet d'ajouter un album picassa avec une URL.")
            self.menuEdit.AppendSeparator()
            self.menuEdit.Append(ID_SYNC, "Actualiser l'album...",
                        "Permet de recharger un album picassa.")
            self.menuEdit.Append(ID_REN, "Renommer l'album...",
                        "Permet de renommer un album picassa.")
            self.menuEdit.Append(ID_SUP, "Supprimer l'album...",
                        "Permet de supprimer un album picassa.")
            self.menuEdit.AppendSeparator()
            self.menuEdit.Append(ID_REC, "Recherche un album",
                        "Permet de rechercher un album picassa.")
            menuBar.Append(self.menuEdit, "&Edition");
            EVT_MENU(self, ID_AJOUT, self.AjoutAlbum)
            EVT_MENU(self, ID_SYNC, self.SyncAlbum)
            EVT_MENU(self, ID_REN, self.RenaAlbum)
            EVT_MENU(self, ID_SUP, self.SuprAlbum)
            EVT_MENU(self, ID_REC, self.RechAlbum)
            
            ''' definition du menu aide '''
            menuAide = wxMenu()
            #menuAide.Append(ID_AIDE, "Aide",
            #            "Affiche une fenetre d'aide du logiciel.")
            #menuAide.AppendSeparator()
            menuAide.Append(ID_ABOUT, "A propos de "+self.PR_NAME+"...",
                        "Plus d'informations sur l'application.")

            menuBar.Append(menuAide, "?");
            EVT_MENU(self, ID_ABOUT, self.OnAbout)
            
            ''' ajout de la barre de menu a la fenetre '''
            self.SetMenuBar(menuBar)  

    ''' Grise ou non les menu (actualiser, renommer et supprimer) suivant le booleen flag''' 
    def cacheMenu(self, flag):
	    if flag:
		flag = False
            else:
		flag = True

	    self.menuEdit.GetMenuItems()[2].Enable(flag)
	    self.menuEdit.GetMenuItems()[3].Enable(flag)
	    self.menuEdit.GetMenuItems()[4].Enable(flag)
                     
    ''' fonction apppele par evenement pour afficher tous les albums '''
    def afficheAlbumsE(self,event):
        self.afficheAlbums()
        
    ''' affiche une message de dialogue definissant l'application '''
    def OnAbout(self, event):
            dlg = wxMessageDialog(self,self.PR_NAME+" :\n\n"
                                      "Ce programme permet de telecharger des albums picassa,\n"
                                      "de les sauvegarder, les visualiser et les supprimer.\n\n"
                                      "Auteurs : \n\n   Maxime Rodrigues,\n   Xavier Mourgues,\n   Sylvain Picarle.",
                                      "A Propos...", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
    
    ''' permet de fermer la fenetre '''
    def TimeToQuit(self, event):
            self.Close(true)
        

    #''' affiche une message de dialogue definissant l'application '''
    #def OnAide(self, event):
    #        dlg = wxMessageDialog(self,self.PR_NAME+" fichier d'aide :\n\n"
    #                                  "Ce programme permet de telecharger des albums picassa,\n"
    #                                  "de les sauvegarder,visualiser et supprimer.\n\n"
    #                                  "By : \n\n   Maxime Rodrigues \n    Xavier Mourgues \n    Sylvain Picalre",
    #                                  "Aide    F1", wxOK | wxICON_INFORMATION)
    #        dlg.ShowModal()
    #        dlg.Destroy()

    ''' permet d'ajouter un album :
            ouvre une fenetre permet de saisir les differents parametre de l'albums
    '''
    def AjoutAlbum(self,event):
            frame = MyAjoutFrame(self,-2,"Ajout d'un album...",ajout_size_x,ajout_size_y )
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
                
                dlg = wxMessageDialog(self,self.PR_NAME+"\n\n"
                                          "La synchronisation est un peu longue suivant le nombre d'images.\n\nCliquez sur valider pour lancer la synchronisation",
                                          "Synchronisation...", wxOK | wxICON_INFORMATION)
        
                dlg.ShowModal()
        	self.MyAlbums.sync(album.getNom())
                dlg.Destroy()
    
    ''' permet de renommer un albums '''
    def RenaAlbum(self,event):
            if self.AlbumEnCours == -1:
                self.MsgAucunSelect()
            else:
                self.AlbumEnCours
                albums = self.MyAlbums.getAlbums()
                album = albums[self.AlbumEnCours]
                #print "Rename de l'album" , album.getNom()
                frame = Rename_Frame(self, -1,"Renommer un album...",album.getNom(),350,180)
                frame.Show(True)
        
    ''' permet de supprimer un albums '''
    def SuprAlbum(self,event):
            if self.AlbumEnCours == -1:
                self.MsgAucunSelect()
            else:
                albums = self.MyAlbums.getAlbums()
                album = albums[self.AlbumEnCours]
                #print "Suppression de l'album",album.getNom()
                frame = Confirme_Supr_Frame(self, -1,"Confirmation de suppression...",album,350,250)
                frame.Show(True)
              
    ''' affiche une erreur comme quoi il faut selectionner un album '''
    def MsgAucunSelect(self):
            dlg = wxMessageDialog(self,self.PR_NAME+"Aucun album n'est selectionne!\n\n"
                                          "Selectionnez un album,\n"
                                          "Si aucun alnum existe, ajoutez en...\n\n",
                                          "Message d'erreur", wxOK | wxICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
    
    
    ''' ------------------------------------------------------------------------------------------------
    ******************** FIN  Initialisation de la barre de menu ***************************************
    ----------------------------------------------------------------------------------------------------
    '''
