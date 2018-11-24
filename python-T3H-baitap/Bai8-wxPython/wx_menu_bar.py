import wx

def OnExit(event):
    frame.Close()

app = wx.App()
frame = wx.Frame(None, title="Vi du Menu", size=(300,150))
panel = wx.Panel(frame, -1)

menuBar = wx.MenuBar()

menu = wx.Menu()
itemExit = wx.MenuItem(menu, -1, text="New", kind= wx.ITEM_NORMAL)
#itemExit.SetBitmap(wx.Bitmap("D:\PYTHON\Python-T3H\ThucHanh\Bai8-wxPython\Media\mini.PNG"))
itemExit.SetBitmap(wx.Bitmap("Media/mini.PNG"))
menu.Append(itemExit)
menuBar.Append(menu, "&File")

menu2 = wx.Menu()
menuBar.Append(menu2, "&Edit")

menu3 = wx.Menu()
menuBar.Append(menu3, "&View")

frame.SetMenuBar(menuBar)
frame.Bind(wx.EVT_MENU, OnExit, itemExit)

frame.Show(True)
app.MainLoop()
