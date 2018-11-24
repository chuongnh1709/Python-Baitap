import wx
# class MyFrame(wx.Frame):   # class MyFram kế thừa từ wx.MyFrame

app = wx.App()
frame = wx.Frame(None, title= "Vi du StaticText", size=(200,100))
panel = wx.Panel(frame)
wx.StaticText(panel, -1, "Trung tam tin hoc", size=(150,30), pos=(50,10))
# -1 : ko chọn ID 
frame.Show(True)
app.MainLoop()

