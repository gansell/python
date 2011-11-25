import xml.etree.ElementTree as ET

tree = ET.parse('cityindex.xml')
root = tree.getroot()
print [ x.text for x in root.findall('entry/city')]