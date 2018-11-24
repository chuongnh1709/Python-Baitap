from xml.dom.minidom import Document
import xml.dom.minidom
import os.path

def make_xml(ten_file):

    if (os.path.isfile(ten_file)):              # kiem tra file co ton tai 
        doc = xml.dom.minidom.parse(ten_file)
         # create Root node 
        root_xml = doc.documentElement
    else: 
        doc = Document()
        root_xml = doc.createElement('books')
        doc.appendChild(root_xml)
    
    # create childnode 
    child_node = doc.createElement('book')
    noi_dung = 'Đường xa con hát'
    child_node.setAttribute('title', noi_dung)   # tạo thuộc tính, đầu tab
    root_xml.appendChild(child_node)

    author = doc.createElement('author')         # tạo node con
    tac_gia = "Đỗ Nhật Nam"
    author.appendChild(doc.createTextNode(tac_gia))     # tạo value cho node con = createTextNode
    child_node.appendChild(author)               # gắn vào node cha (node cha là child node)

    nxb = doc.createElement('NXB')               # tạo node con
    NXB_value = "Kim Đồng"
    nxb.appendChild(doc.createTextNode(NXB_value))     # tạo value cho node con = createTextNode
    child_node.appendChild(nxb)                  # gắn vào node cha (node cha là child node)


    return doc

if __name__ == "__main__":
    make_xml('book_ch.xml').writexml(open(file='book_ch.xml', mode = 'w', encoding ='utf8'), indent='',addindent='', newl='')
