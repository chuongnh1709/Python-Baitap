import wx
app = wx.App()
frame = wx.Frame(None, title='Ví dụ static boxsizer',size=(420,300))
panel = wx.Panel(frame, -1)

vbox = wx.BoxSizer(wx.VERTICAL)
nm = wx.StaticBox(panel, -1, 'Name:')
nmSizer = wx.StaticBoxSizer(nm, wx.VERTICAL)
nmbox = wx.BoxSizer(wx.HORIZONTAL)
fn = wx.StaticText(panel, -1, "First Name", size=(350,-1))
nmbox.Add(fn, 0, wx.ALL|wx.CENTER, 5)
nmSizer.Add(nmbox, 0, wx.ALL| wx.CENTER, 0)
vbox.Add(nmSizer, 0 , wx.ALL| wx.CENTER, 0)
panel.SetSizer(vbox)
frame.Centre()
panel.Fit()

frame.Show(True)
app.MainLoop()
