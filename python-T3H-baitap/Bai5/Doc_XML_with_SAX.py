import xml.sax
import sys

# Hien thi thong tin trong file XML = SAX API
class StudentHandler(xml.sax.ContentHandler):
    sl = 0

    def __init__(self):
        self.CurrentData = ""
        self.phone = ""
        self.name = ""

    # Call when an element starts 
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        print("List of contacts: ")

        if tag == "contact":
            print("--- Contact ", StudentHandler.sl, "---")
            self.name == attributes["name"]
            print("Name : ", self.name)
            self.phone == attributes["phone"]
            print("Phone: ", self.phone)
        StudentHandler.sl += 1

    if(__name__ == "main"):
        # create an XMLReader
        parser = xml.sax.make_parser()
        # turn off namespaces
        parser.setFeature(xml.sax.handler.feature_namespaces,0)

        # overrid the default ContextHandler
        Handler = StudentHandler()
        parser.setContentHandler(Handler)

        parser.parse("contact.xml")
        # parser.parse(open("./files/contact.xml","r"))