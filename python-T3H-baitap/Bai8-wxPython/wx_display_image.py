import wx
app = wx.App()
frame = wx.Frame(None, title="Ví dụ Image", size=(500,400))
panel = wx.Panel(frame, -1)
# hinh = wx.Image("D:\PYTHON\Python-T3H\ThucHanh\Bai8-wxPython\Media\meo.jpg",wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
hinh = wx.Image("D:/PYTHON/Python-T3H/ThucHanh/Bai8-wxPython/Media/meo.jpg",wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
# cả 2 dạng đường dẫn windows/linux đều đc 
stStaticBitmal = wx.StaticBitmap(panel, -1, hinh)

frame.Show(True)
app.MainLoop()
