import wx

def onXem(self):
    dlg = wx.MessageDialog(None, "Slide 1: value = "+ str(slider1.GetRange()),'A Message Box', wx.OK)
    dlg.ShowModal()

app = wx.App()
frame = wx.Frame(None, title="Ví dụ Slide", size=(340,320))
panel = wx.Panel(frame, -1)

slider1 = wx.Slider(panel, -1, 25, 1, 100, pos=(10,10), size=(250,-1), style= wx.SL_HORIZONTAL| wx.SL_AUTOTICKS| wx.SL_LABELS)

slider2 = wx.Slider(panel, -1, 25, 1, 100, pos=(125,50), size=(-1,250), style=wx.SL_VERTICAL | wx.SL_AUTOTICKS| wx.SL_LABELS)

btnXem = wx.Button(panel, label = "Xem",pos=(200,150), size=(50,30))
frame.Bind(wx.EVT_BUTTON, onXem, btnXem)

frame.Show(True)
app.MainLoop()

