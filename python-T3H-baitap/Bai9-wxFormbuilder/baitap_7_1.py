import wx
import wx.xrc
import json 
###########################################################################
## Class cong_ty
###########################################################################

class cong_ty ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1015,493 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Media/Screenshot.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_bitmap1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Ten", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )

		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Địa chỉ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		gbSizer1.Add( self.m_staticText31, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Điện Thoại", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gbSizer1.Add( self.m_staticText4, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_Ten = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,-1 ), 0 )
		gbSizer1.Add( self.m_Ten, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_MaSo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,-1 ), 0 )
		gbSizer1.Add( self.m_MaSo, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_DiaChi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_DiaChi, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_DT = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_DT, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_Mail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_Mail, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_btnCapNhat = wx.Button( self, wx.ID_ANY, u"Cập nhật", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_btnCapNhat, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( gbSizer1 )
		self.Layout()

		# Connect Events
		self.m_btnCapNhat.Bind( wx.EVT_BUTTON, self.OnClick_btn_CapNhat )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClick_btn_CapNhat( self, event ):
		# event.Skip()
		Ten = self.m_Ten.GetValue()
		Ma_so = self.m_MaSo.GetValue()
		Dia_chi = self.m_DiaChi.GetValue()
		Dien_thoai = self.m_DT.GetValue()
		Mail = self.m_Mail.GetValue()
		# doc tu Json 
		f = open('Dulieu/Cong_ty.json', encoding='utf-8')
		noi_dung = json.load(f)
		f.close()
		noi_dung['Ten']=Ten
		noi_dung['Dia_chi']=Dia_chi
		noi_dung['Dien_thoai']=Dien_thoai
		noi_dung['Mail']=Mail
		# ghi xuong json
		f = open('Dulieu/Cong_ty.json','w',encoding='utf-8')
		json.dump(noi_dung, f, indent=4, ensure_ascii=False)
		f.close()

		wx.MessageBox('Da cap nhat file json','Thong bao')


if __name__=='__main__':
	app = wx.App()
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
	frame.Show(True)
	app.MainLoop()