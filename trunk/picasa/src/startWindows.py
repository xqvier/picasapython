#!/usr/bin/python

'''
Created on 8 janv. 2011

@author: Silou
'''
import sys

from wxPython.wx import *


sys.path.append('./frame')
from PrincipalFrame import MyFrame

''' definition des constantes de taille pour la fenetre '''
fen_size_x = 1150
fen_size_y = 800 

if __name__ == '__main__':
    class MyApp(wxApp):
        def OnInit(self):
            frame = MyFrame(NULL, -1, "Picassa Albums",fen_size_x,fen_size_y)
            frame.Show(true)
            #self.SetTopWindow(frame)
            return true
    
    app = MyApp(0)
    app.MainLoop()

pass
