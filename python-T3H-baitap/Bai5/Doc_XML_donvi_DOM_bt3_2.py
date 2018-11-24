import xml.dom.minidom
from files.class_don_vi import * 

def tao_danh_sach_don_vi(list_don_vi):
    DOMTree = xml.dom.minidom.parse("files/don_vi.xml")
    collection = DOMTree.documentElement

    don_vi_s = collection.getElementsByTagName("DON_VI")

    for don_vi in don_vi_s:
        if don_vi.hasAttribute("ID") and don_vi.hasAttribute("Ten"):
            dv = Donvi(don_vi.getAttribute("ID"), don_vi.getAttribute("Ten"))
            list_don_vi.append(dv)

def tao_danh_sach_nhan_vien(list_nhan_vien):
    # DOMTree = xml.dom.minidom.parse("D:/Python-T3H/ThucHanh/Bai5/files/nhan_vien.xml")
    DOMTree = xml.dom.minidom.parse("files/nhan_vien.xml")
    collection = DOMTree.documentElement

    nhan_vien_s = collection.getElementsByTagName("NHAN_VIEN")

    for nhan_vien in nhan_vien_s:
        if nhan_vien.hasAttribute("ID") and nhan_vien.hasAttribute("ID_DON_VI"): # Nhan vien phai thuoc ve 1 don vi nao do, tuc la phai co ID_DON_VI
            nv = NhanVien(nhan_vien.getAttribute("ID"),nhan_vien.getAttribute("Ho_ten"),\
            nhan_vien.getAttribute("Gioi_tinh"),\
            nhan_vien.getAttribute("ngay_sinh"),\
            nhan_vien.getAttribute("CMND"),\
            nhan_vien.getAttribute("Muc_luong"),\
            nhan_vien.getAttribute("Dia_chi") ,\
            nhan_vien.getAttribute("ID_DON_VI"))

            list_nhan_vien.append(nv)

    return 

def thong_ke_nhan_vien_theo_donvi(madv, list_nhan_vien):
    tongsoNV=0
    tongsoNVNam=0
    tongsoNVNu=0

    for nv in list_nhan_vien:
        if nv.iddv==madv:
            tongsoNV+=1
            if nv.gioi_tinh == 'true':
                tongsoNVNam+=1
            else:
                tongsoNVNu+=1
            nv.in_thong_tin()
    
    print("Tong so nv: ", tongsoNV, " so NV nam: ", tongsoNVNam, " so NV nu: ",tongsoNVNu)


def tim_nhan_vien(ten, list_nhan_vien):
    count=0
    ten=ten.lower()
    for nv in list_nhan_vien:
        if nv.ho_ten.lower().find(ten) != -1 :
            count+=1
            nv.in_thong_tin()
    if count == 0:
        print("Khong tim thay nhan vien nay")

if __name__== "__main__":
    list_don_vi=[]
    list_nhan_vien=[]
    tao_danh_sach_don_vi(list_don_vi)
    tao_danh_sach_nhan_vien(list_nhan_vien)

    print("----Danh sac1hc đơn vị----")
    for dv in list_don_vi:
        print(dv.iddv, '-', dv.ten)
    
    #----Thong ke----#
    ma_dv = input("Nhap ma don vi muon in: ")
    thong_ke_nhan_vien_theo_donvi(ma_dv,list_nhan_vien)

    #----Tim nhan vien----#
    ten = input("Nhap ten nhan vien muon tim: ")
    tim_nhan_vien(ten, list_nhan_vien)


            




