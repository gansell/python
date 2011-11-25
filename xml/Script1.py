from lxml import etree

tree = etree.parse('cityindex.xml')
root = tree.getroot()
print [ el.text for el in root.xpath('//city') ]
