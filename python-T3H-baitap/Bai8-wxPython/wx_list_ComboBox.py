import wx

app = wx.App()
frame = wx.Frame(None, title='Vi du Choice',size=(300,150))
panel = wx.Panel(frame, -1)

sampleList = ['zero','one','two','three','four','five','size','seven','eight']
wx.StaticText(panel, -1, "Select one:", (15, 20))
wx.Choice(panel, -1, (85, 18), choices=sampleList)

frame.Show(True)
app.MainLoop()