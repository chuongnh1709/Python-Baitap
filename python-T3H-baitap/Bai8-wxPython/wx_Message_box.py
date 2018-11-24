import wx

def OnXem(event):
    kq = wx.MessageBox("bạn có chắc chắn muốn xóa ko ", "Thông Báo", wx.YES_NO| wx.ICON_INFORMATION)
    if wx.YES==kq:
        strTraLoi.SetLabel("Bạn chọn button YES")
    else:
        strTraLoi.SetLabel("Bạn chọn button NO")

app = wx.App()
frame = wx.Frame(None, title="Ví dụ MessageBox", size=(300,150))
panel = wx.Panel(frame, -1)
btnChon = wx.Button(panel, -1, label="Click vào để xem Message", pos=(10,10))
frame.Bind(wx.EVT_BUTTON, OnXem, btnChon)
strTraLoi = wx.StaticText(panel, -1, pos=(10,50))
frame.Show(True)
app.MainLoop()

