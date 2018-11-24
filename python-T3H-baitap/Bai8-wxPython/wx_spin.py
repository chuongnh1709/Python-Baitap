import wx

app = wx.App()
frame = wx.Frame(None, title='Vi du SpinCtrl', size=(300,150))
panel = wx.Panel(frame, -1)
sc = wx.SpinCtrl(panel, -1, "", pos=(30,20), size=(80, -1))
sc.SetRange(1,100)
sc.SetValue(5)
frame.Show()
app.MainLoop()

