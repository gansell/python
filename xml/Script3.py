import xml.etree.ElementTree as ET

root = ET.Element('personlist')
person = ET.SubElement(root, 'person', id='1234')
ET.SubElement(person, 'firstname').text = 'Hubert'
ET.SubElement(person, 'lastname').text = 'Part1'
ET.SubElement(person, 'title').text = 'Dr'
address = ET.SubElement(person, 'address')
ET.SubElement(address, 'street').text = 'Muthgasse 18'
ET.SubElement(address, 'zip').text = '1190'
ET.SubElement(address, 'city').text = 'Wien'
ET.SubElement(address, 'country', pfx='A').text = 'Osterrich'
birthday = ET.SubElement(person, 'birthday')
ET.SubElement(birthday, 'day').text = '8'
ET.SubElement(birthday, 'month', number='3').text = 'march'
ET.SubElement(birthday, 'year').text = '1949'

print ET.tostring(root)

