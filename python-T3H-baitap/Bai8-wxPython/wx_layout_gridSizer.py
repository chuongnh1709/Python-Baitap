import wx
app = wx.App()
frame = wx.Frame(None, title='Ví dụ grid',size=(300,150))
panel = wx.Panel(frame, -1)
gs = wx.GridSizer(3,4,5,5)
for i in range(1,13):
    btn = "button "+ str(i)
    gs.Add(wx.Button(panel, label = btn), 0, wx.EXPAND)

panel.SetSizer(gs)
frame.Center(wx.BOTH)

frame.Show(True)
app.MainLoop()