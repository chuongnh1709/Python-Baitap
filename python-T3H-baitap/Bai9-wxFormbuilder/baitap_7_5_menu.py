from baitap_7_1 import *
from baitap_7_2 import *
from baitap_7_3 import *
from baitap_7_4_QLTV import *
from baithi_giaiPTb2 import *
import wx
import wx.xrc

###########################################################################
## Class baitap_7_5
###########################################################################

class baitap_7_5 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 883,475 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Thong tin cong ty", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem2 )

        self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Them Nhan Vien", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem4 )

        self.m_menubar1.Append( self.m_menu1, u"Cong Ty" )

        self.m_menu2 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Nhom Tivi", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem5 )

        self.m_menuItem6 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Them Tivi", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem6 )

        self.m_menubar1.Append( self.m_menu2, u"Tivi" )

        self.SetMenuBar( self.m_menubar1 )

        self.m_menu3 = wx.Menu()
        self.m_menuItem7 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Giai PT Bac 2", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.m_menuItem7 )

        self.m_menubar1.Append( self.m_menu3, u"Giai_Phuong_trinh_Bac_2" )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.onClick_TTCongTy, id = self.m_menuItem2.GetId() )
        self.Bind( wx.EVT_MENU, self.onClickThemNhanVien, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.OnClickThemNhomTivi, id = self.m_menuItem5.GetId() )
        self.Bind( wx.EVT_MENU, self.OnClickThemTivi, id = self.m_menuItem6.GetId() )
        self.Bind( wx.EVT_MENU, self.OnClickGiaiPTB2, id = self.m_menuItem7.GetId() )


    def __del__( self ):
        pass


	# Virtual event handlers, overide them in your derived class
    def onClick_TTCongTy( self, event ):
        # event.Skip()
        frame = wx.Frame(None, size=(1015,490))
        panel_cong_ty = cong_ty(frame)
        f = open('Dulieu/Cong_ty.json', encoding='utf-8')
        noi_dung = json.load(f)
        f.close()
        panel_cong_ty.m_Ten.SetValue(noi_dung['Ten'])
        panel_cong_ty.m_MaSo.SetValue(noi_dung['Ma_so'])
        panel_cong_ty.m_MaSo.SetValue(noi_dung['Dia_chi'])
        panel_cong_ty.m_MaSo.SetValue(noi_dung['Dien_thoai'])
        panel_cong_ty.m_MaSo.SetValue(noi_dung['Mail'])
        frame.CenterOnScreen(wx.BOTH)
        frame.Show(True)    


    def onClickThemNhanVien( self, event ):
        # event.Skip()
        frame = wx.Frame(None, size=(588,348), title='Thong tin nhan vien')
        panel = baitap_7_3_input_box(frame)
        frame.Show(True)


    def OnClickThemNhomTivi( self, event ):
        # event.Skip()
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


    def OnClickThemTivi( self, event ):
        # event.Skip()
        panel = baitap_7_4(frame)  
        f = open('Dulieu/Cong_ty.json', encoding='utf-8')
        noi_dung = json.load(f)
        f.close()
        DS_Nhom=[]

        for i in noi_dung['Danh_sach_Nhom_Tivi']:
            DS_Nhom.append(i['Ma_so'])
        panel.m_cboNhomTivi.AppendItems(DS_Nhom)
        frame.Show(True)

    def OnClickGiaiPTB2( self, event ):
        # event.Skip()
        # frame = wx.Frame(None, size=(788,288), title='Giai Phuong Trinh Bac 2')
        panel = baithi_panel(frame)    
        frame.Show(True)


if __name__=='__main__':
    app = wx.App()

    frame = baitap_7_5(None)
    frame.Maximize(True)
    frame.Show(True)
    app.MainLoop()