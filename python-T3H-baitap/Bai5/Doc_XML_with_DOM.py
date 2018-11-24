from xml.dom.minidom import parse
import xml.dom.minidom
 
# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("D:/Python - T3H/ThucHanh/Bai5/student.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element: %s" % collection.getAttribute("shelf"))

# Get all the student in the collection 
students = collection.getElementsByTagName("student")

# print detail of each student.
for student in students:
    print("***** Students***** ")
    if student.hasAttribute("id"):
        print("ID: %s" % student.getAttribute("id"))
    
    name = student.getElementsByTagName('name')[0]
    print('Name: %s ' % name.childNodes[0].data)

    date = student.getElementsByTagName('date')[0]
    print('Date of birth: %s' % date.childNodes[0].data)

