import wx
import wx.xrc
import json

###########################################################################
## Class nhom_tivi
###########################################################################

class nhom_tivi ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nhom Ti Vi" ), wx.VERTICAL )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_StaticText = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Mã", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        self.m_StaticText.Wrap( -1 )

        bSizer6.Add( self.m_StaticText, 0, wx.ALL, 5 )

        self.m_Ma = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        bSizer6.Add( self.m_Ma, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

        self.m_StaticText = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        self.m_StaticText.Wrap( -1 )

        bSizer6.Add( self.m_StaticText, 0, wx.ALL, 5 )

        self.m_Ten = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        bSizer6.Add( self.m_Ten, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


        bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )

        self.m_button4 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        sbSizer4.Add( bSizer5, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer3.Add( sbSizer4, 0, wx.EXPAND, 5 )

        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Danh Sách Nhóm" ), wx.VERTICAL )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        m_lstDSNhomChoices = []
        self.m_lstDSNhom = wx.ListBox( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lstDSNhomChoices, 0 )
        bSizer8.Add( self.m_lstDSNhom, 1, wx.ALL|wx.EXPAND, 5 )


        sbSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )


        bSizer3.Add( sbSizer5, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()

        # Connect Events
        self.m_button4.Bind( wx.EVT_BUTTON, self.OnClick_Them )

    def __del__( self ):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnClick_Them( self, event ):
        # event.Skip()
        Ma = self.m_Ma.GetValue()       # Lấy Value của Text_Control box 
        Ten = self.m_Ten.GetValue()
        # mo file để lấy nội dung cũ 
        f = open('Dulieu/Cong_ty.json', encoding='utf-8')
        noi_dung = json.load(f)
        f.close()

        # bo sung/ them noi dung 
        noi_dung['Danh_sach_Nhom_Tivi'].append({'Ten':Ten, 'Ma_so': Ma})

        # luu noi dung moi 
        f = open('Dulieu/Cong_ty.json', 'w', encoding='utf-8')
        json.dump(noi_dung, f, indent=4, ensure_ascii=False)

        # load lai noi dung moi 
        f = open('Dulieu/Cong_ty.json', encoding='utf-8')
        noi_dung = json.load(f)
        f.close()
        ds_nhom_tv = []
        for i in noi_dung['Danh_sach_Nhom_Tivi']:
            ds_nhom_tv.append(i['Ten'])
        
        self.m_lstDSNhom.Clear()    # Clear Listbox, nếu ok thì nội dung cũ tồn tại với nội dung mới
        
        # panel_nhom_tivi.m_lstDSNhom.AppendItems(ds_nhom_tv) 
        self.m_lstDSNhom.AppendItems(ds_nhom_tv)        


'''Main Function'''

if __name__=='__main__':
    app = wx.App()
    frame = wx.Frame(None, size=(800,450), title='Nhom Tivi')
    panel_nhom_tivi = nhom_tivi(frame)

    f = open('Dulieu/Cong_ty.json', encoding='utf-8')
    noi_dung = json.load(f)
    f.close()

    ds_nhom_tv = []
    for i in noi_dung['Danh_sach_Nhom_Tivi']:
        ds_nhom_tv.append(i['Ten'])
    
    panel_nhom_tivi.m_lstDSNhom.AppendItems(ds_nhom_tv)     # append list item (ds_nhom_tv) 
                                                            # vào List box trên giao diện

    frame.Show(True)
    app.MainLoop()


