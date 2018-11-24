import wx
app = wx.App()
frame = wx.Frame(None, title='Vi du Listbox', size=(500,400))
panel = wx.Panel(frame, -1)

vbox = wx.BoxSizer(wx.VERTICAL)
stHoten = wx.StaticText(panel, label="Họ tên")
vbox.Add(stHoten, 0, wx.ALL|wx.EXPAND| wx.ALIGN_CENTER_HORIZONTAL, 5)
txtHoTen = wx.TextCtrl(panel, -1, size=(200,30))
vbox.Add(txtHoTen, 0, wx.ALL|wx.EXPAND| wx.ALIGN_CENTER_HORIZONTAL, 5)

panel.SetSizer(vbox)

frame.Show(True)
app.MainLoop()
