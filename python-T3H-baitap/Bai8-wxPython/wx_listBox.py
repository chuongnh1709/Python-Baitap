import wx

def onListBox(self):
    dlg = wx.MessageDialog(None, event.GetEventObject().GetStringSelection(),'A Message', wx.OK)
    dlg.ShowModal()

app = wx.App()
frame = wx.Frame(None, title="Vi du TextCtrl",size=(400,150))
panel = wx.Panel(frame, -1)

languages = ['C', 'C++', 'Java', 'Python', 'Perl']
lst = wx.ListBox(panel, size=(100,-1), pos=(10,10), choices= languages, style = wx.LB_SINGLE)

frame.Bind(wx.EVT_LISTBOX, onListBox, lst)
frame.Show()
app.MainLoop()