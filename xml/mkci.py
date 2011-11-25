# -*- coding: utf-8 -*-

import sys
import os.path
from lxml import etree, html, objectify

WIKI_URL = 'http://de.wikipedia.org/wiki/Liste_der_Gro%C3%9Fst%C3%A4dte_in_Deutschland'

def log(message):
    print(message)

def parse_table():
    source_file = 'citylist.html'
    if os.path.isfile(source_file):
        log("Reading %s" % source_file)
        tree = etree.parse(source_file)
    else:
        log("Reading %s" % WIKI_URL)
        tree = etree.parse(WIKI_URL)
        tree.write(source_file, encoding='utf-8')
    html.xhtml_to_html(tree)

    tables = tree.findall('//table')
    tables.sort(key=len)
    table = tables[-1] # longest table
    return table

def convert_table(table):
    entries = [
        [ ((td.text if not len(td) else (td[-1].tail or td[0].text)) or '').replace('.', '').replace(',', '.')
          for td in tr[1:] ]
        for tr in table[1:-1]
        ]
    return entries

def build_xml(entries, with_attributes=True):
    root = objectify.Element('cityindex')
    root.title = 'Index of major German cities'

    for table_entry in entries:
        if len(table_entry) != 11:
            log("Invalid entry, expected 11 items, got %d: %s" % (len(table_entry), table_entry))
            continue
        name, ew1980, ew1990, ew2000, ew2009, ew2010, area, ewkm, ch0010, first, region = table_entry
        entry = etree.SubElement(root, 'entry')
        entry.city = name
        entry.region = region
        entry.country = 'Deutschland'
        entry.area_km2 = area
        if with_attributes:
            entry.inhabitants = [ew1980, ew1990, ew2000, ew2009, ew2010]
            entry.inhabitants[0].set('year', '1980')
            entry.inhabitants[0].set('year', '1990')
            entry.inhabitants[1].set('year', '2000')
            entry.inhabitants[2].set('year', '2009')
            entry.inhabitants[3].set('year', '2010')
        else:
            entry.inhabitants = ew2010
        entry.inhabitants_per_km2 = ewkm
        entry.development_2000_2010 = ch0010.replace(u'\u2212', '-') # fix minus sign
        entry.major_since = first
        entry.description = u'%s ist eine deutsche Großstadt.' % name

    objectify.deannotate(root)
    etree.cleanup_namespaces(root)
    return root

def write_xml(root, target_file='cityindex.xml'):
    log("Writing %s" % target_file)
    etree.ElementTree(root).write(
        target_file, encoding='utf-8', standalone='yes',
        pretty_print=True)

def main():
    write_attributes = '-n' not in sys.argv[1:]
    table = parse_table()
    entries = convert_table(table)
    xml_root = build_xml(entries, write_attributes)
    write_xml(xml_root, target_file = 'cityindex%s.xml' % ('_attrs' if write_attributes else ''))

if __name__ == '__main__':
    main()
