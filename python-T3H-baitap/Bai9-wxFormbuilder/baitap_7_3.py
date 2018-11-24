import wx
import wx.xrc

###########################################################################
## Class baitap_7_3_input_box
###########################################################################
# Nhap thong tin Nhan vien và xử lý Label text box 

class baitap_7_3_input_box ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 588,348 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"THÔNG TIN NHÂN VIÊN", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        self.m_staticText8.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        gbSizer2.Add( self.m_staticText8, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Họ Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        gbSizer2.Add( self.m_staticText9, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Ho_ten = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        gbSizer2.Add( self.m_Ho_ten, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Ma_so = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        gbSizer2.Add( self.m_Ma_so, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Ten_dang_nhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        gbSizer2.Add( self.m_Ten_dang_nhap, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Ho_ten_err = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Ho_ten_err.Wrap( -1 )

        self.m_Ho_ten_err.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        gbSizer2.Add( self.m_Ho_ten_err, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText101.Wrap( -1 )

        gbSizer2.Add( self.m_staticText101, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Ma_so_err = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Ma_so_err.Wrap( -1 )

        self.m_Ma_so_err.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        gbSizer2.Add( self.m_Ma_so_err, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText102 = wx.StaticText( self, wx.ID_ANY, u"Tên đăng nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText102.Wrap( -1 )

        gbSizer2.Add( self.m_staticText102, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Ten_dang_nhap_err = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Ten_dang_nhap_err.Wrap( -1 )

        self.m_Ten_dang_nhap_err.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        gbSizer2.Add( self.m_Ten_dang_nhap_err, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText103 = wx.StaticText( self, wx.ID_ANY, u"Mật khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText103.Wrap( -1 )

        gbSizer2.Add( self.m_staticText103, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Mat_khau_err = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Mat_khau_err.Wrap( -1 )

        self.m_Mat_khau_err.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        gbSizer2.Add( self.m_Mat_khau_err, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText1022 = wx.StaticText( self, wx.ID_ANY, u"Xác nhận MK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1022.Wrap( -1 )

        gbSizer2.Add( self.m_staticText1022, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Mat_khau_XN_err = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Mat_khau_XN_err.Wrap( -1 )

        self.m_Mat_khau_XN_err.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        gbSizer2.Add( self.m_Mat_khau_XN_err, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Mat_khau = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        gbSizer2.Add( self.m_Mat_khau, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_Mat_khau_XN = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        gbSizer2.Add( self.m_Mat_khau_XN, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_button3, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( gbSizer2 )
        self.Layout()

        # Connect Events
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnClick_Them )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnClick_Them( self, event ):
        # event.Skip()
        Ten = self.m_Ho_ten.GetValue()
        Ma_so = self.m_Ma_so.GetValue()
        Ten_dang_nhap = self.m_Ten_dang_nhap.GetValue()
        Mat_khau = self.m_Mat_khau.GetValue()
        Mat_khau_xn = self.m_Mat_khau_XN.GetValue()
        flag=1

        # Reset Label để mỗi lần nhấn Submit lại các dấu * được reset 
        self.m_Ho_ten_err.SetLabel('')
        self.m_Ma_so_err.SetLabel('')
        self.m_Ten_dang_nhap_err.SetLabel('')
        self.m_Mat_khau_err.SetLabel('')
        self.m_Mat_khau_XN_err.SetLabel('')

        if len(Ten)==0:
            self.m_Ho_ten_err.SetLabel('*')
            flag=0
        if len(Ma_so)==0:
            self.m_Ma_so_err.SetLabel('*')
            flag=0
        if len(Ten_dang_nhap)==0:
            self.m_Ten_dang_nhap_err.SetLabel('*')
            flag=0
        if len(Mat_khau)==0:
            self.m_Mat_khau_err.SetLabel('*')
            flag=0
        if Mat_khau_xn != Mat_khau:
            self.m_Mat_khau_XN_err.SetLabel('*')
            flag=0
        if flag==1:
            wx.MessageBox('Cho luu', 'Thong Bao')       # Hiển thị MessageBox, title = Thông báo 


if __name__=='__main__':
    app = wx.App()
    frame = wx.Frame(None, size=(588,348), title='Thong tin nhan vien')
    
    panel = baitap_7_3_input_box(frame)
    frame.Show(True)
    app.MainLoop()

