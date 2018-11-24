import wx
app = wx.App()
frame = wx.Frame(None, title='Ví dụ TextCtrl', size=(300,100))
panel = wx.Panel(frame, -1)
wx.TextCtrl(panel, -1, "nhập họ tên", pos=(50,10), size=(175,30))
frame.Show(True)
app.MainLoop()
