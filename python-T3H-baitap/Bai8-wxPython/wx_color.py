import wx
app = wx.App()
frame = wx.Frame(None, title="Vi du TextCtrl",size=(400,150))
panel = wx.Panel(frame, -1)

stHoTen = wx.StaticText(panel, -1, label="Họ Tên:", pos=(10,10),size=wx.DefaultSize)
stHoTen.SetForegroundColour("#8f3d5e")
txtHoTen = wx.TextCtrl(panel, -1 ,value="nhập họ tên", pos=(100,10),size=(250,30))
txtHoTen.SetForegroundColour("red")

_color = wx.Colour(143,61,94)

stLop = wx.StaticText(panel, -1, label="Lớp:", pos=(10,50))
stLop.SetForegroundColour(_color)
txtLop = wx.TextCtrl(panel, -1, value="nhập lớp", pos=(100,50), size=(250,30))
txtLop.SetForegroundColour(wx.RED)

frame.Show(True)
app.MainLoop()
