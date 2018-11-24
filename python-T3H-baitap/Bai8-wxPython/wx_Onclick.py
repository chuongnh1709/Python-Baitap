import wx
def OnClick(sefl):
    button.SetLabel("Clicked")

app = wx.App()
frame = wx.Frame(None, title="Ví dụ TextCtrl", size=(300,100))
panel = wx.Panel(frame, -1)
button = wx.Button(panel, -1, "Hello", pos=(50,20))

frame.Bind(wx.EVT_BUTTON, OnClick, button)  # khi bấm vào button thì thực hiện sự kiện OnClick -> đổi tên thành Click 
button.SetDefault()

frame.Show()
app.MainLoop()

