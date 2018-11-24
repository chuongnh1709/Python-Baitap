import wx

app = wx.App()
frame = wx.Frame(None,title="Ví dụ Checkbox", size=(300,150))
panel = wx.Panel(frame, -1)

radio1 = wx.RadioButton(panel, -1, "Nữ", pos=(20, 10))
radio2 = wx.RadioButton(panel, -1, "Nam", pos=(20, 40))
radio3 = wx.RadioButton(panel, -1, "Khác", pos=(20, 70))

frame.Show(True)
app.MainLoop()
