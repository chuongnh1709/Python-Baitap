import wx
import wx.xrc
import json
import sqlite3
###########################################################################
## Class baitaP_7_4
###########################################################################
class baitap_7_4 ( wx.Panel ):
    
    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 817,365 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        gbSizer3 = wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Thong Tin TV", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        self.m_staticText19.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        gbSizer3.Add( self.m_staticText19, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Ma So", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )

        gbSizer3.Add( self.m_staticText20, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Ten", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        gbSizer3.Add( self.m_staticText21, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_txtTen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.m_txtTen, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Ky Hieu", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        gbSizer3.Add( self.m_staticText22, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_txtKyHieu = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.m_txtKyHieu, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Don gia nhap", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )

        gbSizer3.Add( self.m_staticText23, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_txtDongianhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.m_txtDongianhap, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Don gia ban", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )

        gbSizer3.Add( self.m_staticText24, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_txtDongiaban = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
        gbSizer3.Add( self.m_txtDongiaban, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"So luong ton", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )

        gbSizer3.Add( self.m_staticText25, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_cboNhomTivi = wx.Button( self, wx.ID_ANY, u"Them", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.m_cboNhomTivi, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 7 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_txtSoluongton = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.m_txtSoluongton, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Nhom tivi", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )

        gbSizer3.Add( self.m_staticText26, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        m_cboNhomTiviChoices = []
        self.m_cboNhomTivi = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_cboNhomTiviChoices, 0 )
        self.m_cboNhomTivi.SetSelection( 0 )
        gbSizer3.Add( self.m_cboNhomTivi, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_txtMaSo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
        gbSizer3.Add( self.m_txtMaSo, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        self.SetSizer( gbSizer3 )
        self.Layout()

        # Connect Events
        self.m_cboNhomTivi.Bind( wx.EVT_BUTTON, self.OnClick_Them )

    def __del__( self ):
        pass

    def OnClick_Them(self, event):
        ma_so = self.m_txtMaSo.GetValue()
        ten = self.m_txtTen.GetValue()
        ky_hieu = self.m_txtKyHieu.GetValue()
        don_gia_ban = self.m_txtDongiaban.GetValue()
        don_gia_nhap = self.m_txtDongianhap.GetValue()
        so_luong_ton = self.m_txtSoluongton.GetValue()
        nhom_tivi = self.m_cboNhomTivi.GetValue()

        conn = sqlite3.connect('Dulieu/product.db')
        chuoiSQL = 'insert into tblTivi(Ma_so, Ten, Ky_hieu, Don_Gia_Nhap, Don_Gia_Ban, So_Luong_Ton, Nhom_Tivi) values (?,?,?,?,?,?,?)'
        conn.execute(chuoiSQL,(ma_so, ten, ky_hieu, don_gia_nhap, don_gia_ban, so_luong_ton, nhom_tivi))
        conn.commit()
        conn.close()

if __name__ =="__main__":
    app = wx.App()
    frame = wx.Frame(None, size=(817,365), title='Thong tin TiVi')
    
    panel = baitap_7_4(frame)
    
    f = open('Dulieu/Cong_ty.json', encoding='utf-8')
    noi_dung = json.load(f)
    f.close()
    DS_Nhom=[]

    for i in noi_dung['Danh_sach_Nhom_Tivi']:
        DS_Nhom.append(i['Ma_so'])
    panel.m_cboNhomTivi.AppendItems(DS_Nhom)
    frame.Show(True)
    
    app.MainLoop()
