import wx
import wx.xrc
import math
import json 

###########################################################################
## Class baithi_panel
###########################################################################
# Giai Phuong trinh bac 2 

class baithi_panel ( wx.Panel ):
    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 788,288 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        gbSizer5 = wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.BOTH )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Giai phuong trinh bac hai\n      (ax^2 + bx + c=0)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27.Wrap( -1 )

        self.m_staticText27.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        gbSizer5.Add( self.m_staticText27, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 7 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"a=", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText28.Wrap( -1 )

        gbSizer5.Add( self.m_staticText28, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_text_A = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer5.Add( self.m_text_A, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"b=", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText29.Wrap( -1 )

        gbSizer5.Add( self.m_staticText29, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_text_B = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer5.Add( self.m_text_B, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText_NghiemPT = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_NghiemPT.Wrap( -1 )

        gbSizer5.Add( self.m_staticText_NghiemPT, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"c=", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText30.Wrap( -1 )

        gbSizer5.Add( self.m_staticText30, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button5 = wx.Button( self, wx.ID_ANY, u"Tim Nghiem", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_button5, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 7 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_text_C = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer5.Add( self.m_text_C, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        self.SetSizer( gbSizer5 )
        self.Layout()

        # Connect Events
        self.m_button5.Bind( wx.EVT_BUTTON, self.OnClick_TimNghiem )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnClick_TimNghiem( self, event ):
        a = int(self.m_text_A.GetValue())
        b = int(self.m_text_B.GetValue())
        c = int(self.m_text_C.GetValue())
        danh_sach_phuong_trinh = {}

        if a==0:
            self.m_staticText_NghiemPT.SetLabel("Nhap a != 0 ")
            danh_sach_phuong_trinh= {
                'a':a ,
                'b':b ,
                'c':c ,
                'nghiem' :"phuong trinh co he so a=0, ko hop le"
                }            
        else: 
            delta = b*b - 4*a*c
            if delta > 0 :
                x1 = (-b + math.sqrt(delta))/(2*a)
                x2 = (-b - math.sqrt(delta))/(2*a)
                self.m_staticText_NghiemPT.SetLabel("Phuong trinh co 2 nghiem phan biet : x1= %3.2f x2= %3.2f " %(x1,x2))
                danh_sach_phuong_trinh = {'a':a ,'b':b ,'c':c ,'nghiem' :"Phuong trinh co 2 nghiem phan biet : x1= %3.2f x2= %3.2f " %(x1,x2)}              
            elif delta ==0 :
                self.m_staticText_NghiemPT.SetLabel("phuong trinh co nghiem kep x1=x2= %3.1f" %(-b/2*a))
                danh_sach_phuong_trinh= {
                'a':a ,
                'b':b ,
                'c':c ,
                'nghiem' :"phuong trinh co nghiem kep x1=x2= %3.1f" %(-b/2*a)
                }
            else :
                self.m_staticText_NghiemPT.SetLabel("phuong trinh vo nghiem")
                danh_sach_phuong_trinh = {
                'a':a ,
                'b':b ,
                'c':c ,
                'nghiem' :"phuong trinh vo nghiem"
                }
                
        print(danh_sach_phuong_trinh)
        # return danh_sach_phuong_trinh

        # Open Json 
        f = open('Dulieu/Phuong_trinh_bac_2.json', encoding='utf-8')
        noi_dung = json.load(f)
        f.close()
        print(noi_dung)

        # bo sung/ them noi dung 
        noi_dung['danh_sach_phuong_trinh'].append(danh_sach_phuong_trinh)
        print(noi_dung)

        # luu noi dung moi 
        f = open('Dulieu/Phuong_trinh_bac_2.json', 'w', encoding='utf-8')
        json.dump(noi_dung, f, indent=4, ensure_ascii=False)
        f.close()

'''
Main Function  
'''
if __name__=='__main__':
    app = wx.App()
    frame = wx.Frame(None, size=(788,288), title='Giai Phuong Trinh Bac 2')
    panel = baithi_panel(frame)    

    frame.Show(True)
    app.MainLoop()
