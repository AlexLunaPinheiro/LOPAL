import xml.etree.cElementTree as ET



root = ET.Element("Config")
version = ET.SubElement(root,"Versao")
version.text = "1.0"
tree =ET.ElementTree(root)
tree.write("config.xml")


arvore = ET.parse('config.xml')

raiz = arvore.getroot()

print(raiz.tag)