# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"R&CS TOES Controller"), pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        fgSizer1 = wx.FlexGridSizer( 2, 3, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.BN_101 = wx.Button( self, wx.ID_ANY, _(u"Cmd 101"), wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.BN_101, 0, wx.ALL, 5 )

        self.BN_102 = wx.Button( self, wx.ID_ANY, _(u"Cmd 102"), wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.BN_102, 0, wx.ALL, 5 )

        self.BBN_103 = wx.Button( self, wx.ID_ANY, _(u"Cmd 103"), wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.BBN_103, 0, wx.ALL, 5 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )


        bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )

        self.TC_Debug = wx.TextCtrl( self, wx.ID_ANY, _(u"Test From Brad"), wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer1.Add( self.TC_Debug, 3, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.BN_101.Bind( wx.EVT_BUTTON, self.BN_101OnButtonClick )
        self.BN_102.Bind( wx.EVT_BUTTON, self.BN_102OnButtonClick )
        self.BBN_103.Bind( wx.EVT_BUTTON, self.BBN_103OnButtonClick )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def BN_101OnButtonClick( self, event ):
        event.Skip()

    def BN_102OnButtonClick( self, event ):
        event.Skip()

    def BBN_103OnButtonClick( self, event ):
        event.Skip()


